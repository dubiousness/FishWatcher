#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import json
import time

class Sender():
    def __init__(self):
        print("start sender...")
        self.read_setting()
        self.socket = socket.socket()

    def read_setting(self):
        setting = json.load(open('setting.json'))
        
        self.PORT = int(setting['PORT'])
        self.HOST = str(setting['HOST'])
        self.INTERVAL = float(setting['INTERVAL'])

        print("")
        print("--SETTING--")
        print("HOST: {0}".format(self.HOST))
        print("PORT: {0}".format(self.PORT))
        print("INTERVAL: {0}".format(self.INTERVAL))
        print("")

    def connect(self):
        try:
            self.socket.connect((self.HOST, self.PORT))
            print("connect!")
        except:
            print("fail!")

    def sidconnect(self):
        self.socket.close()

    def send(self, rec):
        self.socket.send(rec.encode("utf-8"))
        time.sleep(self.INTERVAL)

if __name__ == '__main__':
    s = Sender()
    s.connect()
    for i in range(100):
        s.send(str(i))
    s.disconnect()
