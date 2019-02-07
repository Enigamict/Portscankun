# -*- coding: utf-8 -*-
import socket
import argparse
from scapy.all import *

def op():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tcp",help="TCPで直接繋いでスキャンします",action="store_true")
    parser.add_argument("--syn",help="ハーフスキャンします",action="store_true")
    args = parser.parse_args()
    return args

def tcp():
    args = op()
    if args.tcp:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpip = input("InputTARGETIP>> ")
        tcpport = input("InputTARGETPort>> ")
        code = sock.connect_ex((tcpip,int(tcpport)))
        sock.close()
        if code == 0:
            print(f"{tcpport}OPEN")
        if code != 0:
            print(f"{tcpport}Close")

def tcpsyn():
    args = op()
    if args.syn:
        local_ip = socket.gethostbyname(socket.gethostname())
        sikensu = random.randint(0, 1000)
        targetip = input("InputTARGETIP>> ")
        synport = input("InputTARGETPort>> ")
        ip=IP(src=local_ip,dst=targetip)
        syn=TCP(sport=RandShort(),dport=int(synport),flags='S',seq=sikensu)
        syns=sr1(ip/syn,timeout=30)
        if str(type(syns)) == "<class 'scapy.layers.inet.IP'>":
            print(f"{synport}:OPEN")
        else:
            print(f"{synport}:ClOSE")

    

if __name__ == '__main__':
    op()
    tcp()
    tcpsyn()
