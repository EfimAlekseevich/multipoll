from abc import ABC, abstractmethod
import struct


class Datatype(ABC):
    '''Datatype'''
    name = ''
    size = 1
    signed = True

    @abstractmethod
    def unpack(cls, data_bytes, bytes_order):
        pass


class USInt(Datatype):
    '''
    USInt -- unsigned short integer 16 bits = 2 bytes
    Min = 0, Max = 2**16 - 1 =  65 535
    '''
    name = 'USInt'
    size = 1
    signed = False

    @classmethod
    def unpack(cls, data_bytes, byte_order=(0, 1)):
        ordered_bytes = bytearray((data_bytes[byte_order[0]],
                                   data_bytes[byte_order[1]]))
        value = struct.unpack('H', ordered_bytes)
        return value[0]


class UInt(Datatype):
    '''
    UInt -- unsigned integer 32 bits = 4 bytes
    Min = 0, Max = 2**32 - 1 =  4 294 967 295
    '''
    name = 'UInt'
    size = 2
    signed = False

    @classmethod
    def unpack(cls, data_bytes, bytes_order=(0, 1, 2, 3)):
        ordered_bytes = bytearray((data_bytes[bytes_order[0]],
                                   data_bytes[bytes_order[1]],
                                   data_bytes[bytes_order[2]],
                                   data_bytes[bytes_order[3]]))
        value = struct.unpack('I', ordered_bytes)
        return value[0]


class Real(Datatype):
    '''Real'''
    name = 'Real'
    size = 2
    signed = True

    @classmethod
    def unpack(cls, data_bytes, bytes_order=(0, 1, 2, 3)):
        ordered_bytes = bytearray((data_bytes[bytes_order[0]],
                                   data_bytes[bytes_order[1]],
                                   data_bytes[bytes_order[2]],
                                   data_bytes[bytes_order[3]]))
        value = struct.unpack('f', ordered_bytes)
        return value[0]
