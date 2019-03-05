# Portscankun  
[![MIT License](https://img.shields.io/badge/Scapy-2.4.2-green.svg)](https://scapy.readthedocs.io/en/latest/)  
目標のポートが開いているか閉じているかを判断します。    
### OPTION  
`--tcp`  
ソケット通信をTCPで展開し、connect_exメソッドを使って直接的に通信を行いポートをスキャンします。  
`--syn`  
Scapyを使用し、SYNパケットをターゲットに送信し実際に通信しているようにみせかけた(3-way-handshakeを完全に行わない)スキャン方法です。ハーフスキャンと呼ばれるものです(到達可能なポートではあるがそこで待機しているアプリケーションが無い場合でもopen状態と判断しています。ガバです)  
`--port PORT`  
ポート番号を指定。    
`--ip IP`  
IP&ホスト名を指定。
