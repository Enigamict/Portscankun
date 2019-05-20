# -*- coding: utf-8 -*-
import socket
import argparse
from scapy.all import *
import threading

def op():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tcp",help="TCPで直接繋いでスキャンします",action="store_true")
    parser.add_argument("--syn",help="ハーフスキャンします",action="store_true")
    parser.add_argument("--ip", help="IP&ホストを指定")
    parser.add_argument("--port", help="スキャンする範囲を指定")
    args = parser.parse_args()
    return args

args = op()

def tcp(ports1):
    if args.tcp:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code = sock.connect_ex((args.ip, ports1))
        if code is 0:
            print(f"{ports1}/tcp Open")

def syn(ports):
    if args.syn:
        sikens = random.randint(0, 1000)
        syn=IP(dst=args.ip)/TCP(sport=RandShort(),dport=ports,flags='S',seq=sikens)
        syns=sr1(syn, timeout=5, verbose =0)
        if str(type(syns)) == "<class 'NoneType'>":
            pass
        elif syns[TCP].flags == "SA":
            print(f"{ports}/tcp Open")
        elif syns[TCP].flags == "RA":
            print(f"{ports}/tcp Closed")

for port in range(1, args.port):
    thread = threading.Thread(target=syn, args=(port, ))
    thread1 = threading.Thread(target=tcp, args=(port, ))
    thread.start()
    thread1.start()

if __name__ == '__main__':
    op()
