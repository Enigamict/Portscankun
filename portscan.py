# -*- coding: utf-8 -*-
import socket

host = input("IPまたはホスト入力>> ")
data = input("ポート入力>> ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
code = sock.connect_ex((host, int(data)))
sock.close()

if code == 0:
    print(f"{data}は開いています")
if code != 0:
    print(f"{data}は開いていないよ！")