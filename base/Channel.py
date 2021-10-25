import os
from datetime import datetime
from base.defines import status
from yaml import YAMLObject


class Channel(YAMLObject):
    '''Channel'''

    ids = 0

    loss_limit = 50
    delay_limit = 1000
    status_list = status['channel']

    def __init__(self, name, ip, port=502, timeout=1, country=None, city=None, desc=''):
        '''
        :param name:
        :param ip:
        :param port:
        :param timeout:
        :param country:
        :param city:
        '''

        # Channel description
        self.name = name
        self.country = country
        self.city = city
        self.desc = desc

        # Channel configurations
        self.ip = ip
        self.port = port
        self.timeout = timeout

        # Channel status and statistics
        self.status = self.status_list[0]
        self.delay = -1
        self.last_upd = -1
        self.active_devices = 0

        # Channel id
        self.id = self.ids
        self.ids += 1

        self.update()

    def __del__(self):
        self.ids -= 1

    def update(self):
        ping_result = self.ping(self.ip, timeout=self.timeout*1000+1000)
        self.delay = ping_result['Average delay, ms']
        if self.delay == -1:
            self.status = self.status_list[1]
        elif ping_result['Average delay, ms'] > self.delay_limit or ping_result['Loss, %'] > self.loss_limit:
            self.status = self.status_list[2]
        else:
            self.status = self.status_list[3]
        self.last_upd = datetime.now()

    def __str__(self):
        return f'{self.name} | {self.ip}:{self.port} | {self.status} | Devices: {self.active_devices} | {self.desc} '

    def __repr__(self):
        return str(self)

    @staticmethod
    def ping(ip, count=4, size=32, timeout=1000):
        response = os.popen(f"ping -n {count} -l {size} -w {timeout} {ip}").readlines()
        result = {}
        if 'Approximate round trip times in milli-seconds:\n' in response:
            result['Average delay, ms'] = int(response[-1].split(',')[-1].split('=')[-1][:-3])
            result['Loss, %'] = int(response[-3].split(',')[-2].split('(')[-1].split('%')[0])
        else:
            result['Average delay, ms'] = -1
            result['Loss, %'] = int(response[-1].split(',')[-2].split('(')[-1].split('%')[0])

        return result


# chan = Channel('Borisov', '172.17.16.250')
#
# print(chan)
# print(chan.__dict__)
