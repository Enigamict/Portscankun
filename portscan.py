# -*- coding: utf-8 -*-
import socket
import argparse
from scapy.all import *
import threading

def op():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="IP&ホストを指定")
    args = parser.parse_args()
    return args

args = op()

def syn(ports):
    sikens = random.randint(0, 1000)
    syn=IP(dst=args.ip)/TCP(sport=RandShort(),dport=ports,flags='S',seq=sikens)
    syns=sr1(syn, timeout=5, verbose =0)
    if str(type(syns)) == "<class 'NoneType'>":
        pass
    elif syns[TCP].flags == "SA":
        print(f"{ports}/tcp Open")
    elif syns[TCP].flags == "RA":
        print(f"{ports}/tcp Closed")

for port in range(1, 9999):
    thread = threading.Thread(target=syn, args=(port, ))
    thread.start()

if __name__ == '__main__':
    op()
