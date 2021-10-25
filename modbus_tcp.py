import socket
from modbus_tk.defines import *
from base.defines import *


def get(ip, port=MODBUS_TCP_PORT, modbus_id=1, func_type=READ_HOLDING_REGISTERS, address=0, size=1,
        transaction_id=TRANSACTION_ID):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    MBAP_header = bytearray(
        int.to_bytes(transaction_id, 2, 'big') + b'\x00\x00' + b'\x00\x06' + int.to_bytes(modbus_id, 1, 'big'))
    body = bytearray(int.to_bytes(func_type, 1, 'big') +
                     int.to_bytes(address, 2, 'big') +
                     int.to_bytes(size, 2, 'big'))
    request = MBAP_header + body
    s.sendall(bytes(request))
    data = s.recv(1024)
    s.close()
    return data[9:]
