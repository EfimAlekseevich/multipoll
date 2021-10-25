from datetime import datetime
import modbus_tcp


class Device:
    '''Device'''

    ids = 0

    status_dict = {
        -1: 'Not checked',
        0: 'OK',
        1: 'No connection',
        2: 'Problems with some tags'
    }

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

    def update(self):
        self.channel.update()
        if self.channel.status:
            self.status = 1_000_000
        else:
            self.status = 0
        self.last_upd = datetime.now()
        self.status += self.read_all_tags()

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
