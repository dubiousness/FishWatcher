#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import json

def p(msg):
    print("receiver: {0}".format(msg))

class Receiver():
    host = ''
    port = 50005
    rec_stack = []

    def __init__(self):
        p("constraction")

        setting = json.load(open("setting.json"))

        self.port = int(setting["PORT"])
        self.host = str(setting["HOST"])

        print("setting")
        print(self.port)
        print(self.host)
        print("setting")

        p("try binding receiver")
        self._r = socket.socket()
        self._r.bind((self.host, self.port))
        p("binding succeeded!")

        while True:
            self._r.listen(10)
            p("listening...")

            s, addr = self._r.accept()
            p("accept sender!")

            p("start receiving message")
            while True:
                try:
                    msg = s.recv(4096)
                    msg = msg.decode('utf-8')
                    if msg == '':
                        p("sender is close")
                        break
                    print("message: {0}".format(msg))
                    self.rec_stack.append(msg)
                    if len(self.rec_stack) == 100:
                        print(self.rec_stack)
                        with open("log.txt", "w") as f:
                            for rec in self.rec_stack:
                                f.write(rec + "\n")
                        self.rec_stack = []
                except:
                    p("sender is close")
                    break
