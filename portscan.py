# -*- coding: utf-8 -*-
import socket
import argparse
from scapy.all import *

def op():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tcp",help="TCPでスキャンします",action="store_true")
    parser.add_argument("--udp",help="UDPでスキャンします",action="store_true")
    parser.add_argument("--syn",help="SYN形式でスキャンします",action="store_true")
    args = parser.parse_args()
    return args

def tcp():
    args = op()
    if args.tcp:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpip = input("InputIP>> ")
        tcpport = input("InputPort>> ")
        code = sock.connect_ex((tcpip,int(tcpport)))
        sock.close()
        if code == 0:
            print(f"{tcpport}OPEN")
        if code != 0:
            print(f"{tcpport}Close")

def udp():
    args = op()
    if args.udp:
        udpip = input("InputIP>> ")
        udpport = input("InputPort>> ")
        uport = IP(dst=udpip)/UDP(sport=0,dport=int(udpport))
        send(uport)
        uport.show()

def syn():
    args = op()
    if args.syn:
        synip = input("InputIP>> ")
        synport = input("InputPort>> ")
        frame = IP(dst=synip)/TCP(flags = "S",sport=0,dport=int(synport))
        send(frame)
        frame.show()

    

if __name__ == '__main__':
    op()
    tcp()
    udp()
    syn()
