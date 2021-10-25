from datetime import datetime
from base.defines import status
import modbus_tcp
from yaml import YAMLObject


class Device(YAMLObject):
    '''Device'''

    ids = 0
    status_list = status['device']

    def __init__(self, name, modbus_id, tags, channel, desc=''):
        '''

        :param name:
        :param modbus_id:
        :param tags:
        :param channel:
        :param desc:
        '''

        # Describtion
        self.name = name
        self.desc = desc

        # Parameters
        self.modbus_id = modbus_id
        self.tags = tags
        self.channel = channel

        # Status
        self.status = -1
        self.connection = -1
        self.last_upd = -1

        # Id
        self.channel.active_devices += 1
        self.id = self.ids
        self.ids += 1

    def __del__(self):
        self.ids -= 1
        self.channel.active_devices -= 1

    def __str__(self):
        return f'{self.name} | Id:{self.modbus_id} | Tags: {len(self.tags)} | {self.desc}'

    def __repr__(self):
        return str(self)

    def update(self):
        self.channel.update()
        if self.channel.status:
            self.status = 1
        else:
            self.status = 0
        self.last_upd = datetime.now()
        self.read_all_tags()


    def generate_pockets(self):
        pockets = []
        max_size = 256
        first_reg = 1_000_000
        last_reg = 0
        for tag in self.tags:
            pass

    def read_all_tags(self):
        error_counter = 0
        for tag in self.tags:
            error_counter += self.read_tag(tag)
        return error_counter

    def get_response(self, tag):

        response = modbus_tcp.get(self.channel.ip, self.channel.port,
                                  self.modbus_id,
                                  tag.register_type, tag.address, tag.datatype.size)
        return response

    def read_tag(self, tag):
        error = False
        try:
            data = self.get_response(tag)
            tag.data = data
            tag.value = tag.datatype.unpack(data, tag.bytes_order)
        except Exception as e:
            error = True
            print(e)
        finally:
            if not error:
                return 0
            else:
                return 1
