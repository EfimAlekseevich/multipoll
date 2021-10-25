from pprint import pprint
from modbus_tk.defines import *
from base.defines import *

from base.Device import Device
from base.Tag import Tag
from base.Channel import Channel
from base.Datatypes import USInt, UInt, Real
from yaml import dump


channel = Channel('Borisov', '179.179.16.250', 502)
tags = [Tag('P1', 20, Real, b1032, HOLDING_REGISTERS),
        Tag('P2', 2, USInt, b10, HOLDING_REGISTERS),
        Tag('P3', 4, UInt, b1032, HOLDING_REGISTERS),
        Tag('P3', -10, UInt, b1032, HOLDING_REGISTERS)]

plc = Device('M221', 1, tags[:], channel)


def main():
    #plc.update()
    pprint(plc)
    pprint(plc.__dict__)
    print(dump(plc))
    #pprint(plc.channel.__dict__)
    # for tag in plc.tags:
    #     pprint(tag.__dict__)


if __name__ == '__main__':
    main()
