# -*- coding: utf-8 -*-
import socket

def tcp():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpip = input("InputIP>> ")
        tcpport = input("InputPort>> ")
        code = sock.connect_ex((tcpip,int(tcpport)))
        sock.close()
        if code == 0:
            print(f"{tcpport}:OPEN")
        if code != 0:
            print(f"{tcpport}:Close")


if __name__ == '__main__':
    tcp()
