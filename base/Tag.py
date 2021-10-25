from yaml import YAMLObject


class Tag(YAMLObject):
    '''Tag -- description variable in device'''

    ids = 0

    def __init__(self, name, address, datatype, bytes_order, register_type, write=False, desc=''):
        '''

        :param name:
        :param address:
        :param datatype:
        :param bytes_order:
        :param register_type:
        :param write:
        '''

        # Description
        self.name = name
        self.desc = desc

        # Parameters
        self.address = address
        self.datatype = datatype
        self.bytes_order = bytes_order
        self.register_type = register_type

        # Data
        self.data = None
        self.value = None

        # Status and configurations
        self.write = write
        self.last_read = -1
        self.last_writ = -1
        self.status = -1

        # Id
        self.id = self.ids
        self.ids += 1

    def __del__(self):
        self.ids -= 1

    def __str__(self):
        return f'{self.name} | {self.datatype.name} | Address: {self.address}'

    def __repr__(self):
        return str(self)
