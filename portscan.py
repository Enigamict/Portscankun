# -*- coding: utf-8 -*-
import socket
import argparse
from scapy.all import *

def op():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tcp" ,help="TCPで直接繋いでスキャンします",action="store_true")
    parser.add_argument("--syn", help="ハーフスキャンします",action="store_true")
    parser.add_argument("--port", type=int, help="ポート番号を指定")
    parser.add_argument("--ip", help="IP&ホストを指定")
    args = parser.parse_args()
    return args

def tcp():
    args = op()
    if args.tcp:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code = sock.connect_ex((args.ip,args.port))
        sock.close()
        if code == 0:
            print(f"{args.port}/tcp Open")
        if code != 0:
            print(f"{args.port}/tcp Close")

def tcpsyn():
    args = op()
    if args.syn:
        sikens = random.randint(0, 1000)
        syn=IP(dst=args.ip)/TCP(sport=RandShort(),dport=args.port,flags='S',seq=sikens)
        syns=sr1(syn, timeout=30)
        if str(type(syns)) == "<class 'scapy.layers.inet.IP'>":
            print(f"{args.port}/tcp Open")
        else:
            print(f"{args.port}/tcp Close")

    

if __name__ == '__main__':
    op()
    tcp()
    tcpsyn()
