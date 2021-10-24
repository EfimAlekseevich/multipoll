import socket
from modbus_tk.defines import *

MODBUS_TCP_PORT = 502


def get(ip, port=MODBUS_TCP_PORT, id=1, func_type=READ_HOLDING_REGISTERS, address=0, size=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    MBAP_header = bytearray(b'\x00\x01' + b'\x00\x00' + b'\x00\x06' + int.to_bytes(id, 1, 'big'))
    body = bytearray(int.to_bytes(func_type, 1, 'big') +
                     int.to_bytes(address, 2, 'big') +
                     int.to_bytes(size, 2, 'big'))
    request = MBAP_header + body
    s.sendall(bytes(request))
    data = s.recv(1024)
    s.close()
    return data[9:]
