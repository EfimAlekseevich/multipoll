import socket


def main():
    ip = '172.17.16.250'
    modbus_port = 502

    Transaction_ID = 0x0
    Protocol_ID = 0x0
    Length = 0x0
    Unit_ID = 0x1
    # Запрос
    # 0001 0000 0006 11	03 006B 0003
    MBAP_header = bytearray(b'\x00\x01\x00\x00\x00\x06\x01\x03\x00\x00\x00\x30')
    print(MBAP_header)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = s.connect((ip, modbus_port))
    print(conn)
    s.sendall(MBAP_header)
    print('sanded')
    data = s.recv(1024)
    s.close()
    print('Received', data)
    # В ответе от Modbus TCP Slave устройства мы получим:
    #
    # 0001 0000 0009 11 03 06 022B 0064 007F
    answer = {}
    answer['Transaction ID'] = data[0] * 256 + data[1]
    answer['Protocol ID'] = data[2] * 256 + data[3]
    answer['Length'] = data[4] * 256 + data[5]
    answer['Unit ID'] = data[6]
    answer['Functional code'] = data[7]
    answer['Bytes data length'] = data[8]
    answer['Data'] = []
    for byte in data[9:]:
        answer['Data'].append(byte)
    answer['Words'] = []
    for index in range(0, len(answer['Data']), 2):
        answer['Words'].append(answer['Data'][index] * 0xff + answer['Data'][index + 1])
    import pprint

    pprint.pprint(answer)


if __name__ == '__main':
    main()


def get(channel, id, tag):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((channel.ip, channel.port))
    MBAP_header = bytearray(b'\x00\x01' + b'\x00\x00' + b'\x00\x06' + int.to_bytes(id, 1, 'big'))
    body = bytearray(int.to_bytes(tag.register_type, 1, 'big') + int.to_bytes(tag.register, 2, 'big') + int.to_bytes(
        tag.datatype.size, 2, 'big'))
    request = MBAP_header + body
    s.sendall(bytes(request))
    data = s.recv(1024)
    s.close()
    return bytearray(data[9:])
