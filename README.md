# Portscankun  
[![MIT License](https://img.shields.io/badge/Scapy-2.4.2-green.svg)](https://scapy.readthedocs.io/en/latest/)  
目標のポートが開いているか閉じているかを判断します。   
このスクリプトでスキャン使用されているスキャン方法はScapyを使用し、SYNパケットをターゲットに送信し実際に通信しているようにみせかけた(3-way-handshakeを完全に行わない)スキャン方法です。ハーフスキャンと呼ばれるものです。  
### OPTION   
`--ip IP`  
IP&ホスト名を指定。
