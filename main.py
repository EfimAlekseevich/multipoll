from pprint import pprint
from modbus_tk.defines import *

from Device import Device
from Tag import Tag
from Channel import Channel
from Datatypes import USInt, UInt, Real

channel = Channel('Borisov', '172.17.16.250', 502)
tags = [Tag('P1', 20, Real, bytes_order=(1, 0, 3, 2), register_type=HOLDING_REGISTERS),
        Tag('P2', 2, USInt, bytes_order=(1, 0), register_type=HOLDING_REGISTERS),
        Tag('P3', 4, UInt, bytes_order=(0, 1, 2, 3), register_type=HOLDING_REGISTERS),
        Tag('P3', -10, UInt, bytes_order=(0, 1, 2, 3), register_type=HOLDING_REGISTERS)]

plc = Device('M221', 1, tags, channel)


def main():
    plc.update()
    pprint(plc.__dict__)
    # pprint(plc.channel.__dict__)
    # for tag in plc.tags:
    #     pprint(tag.__dict__)


if __name__ == '__main__':
    main()
