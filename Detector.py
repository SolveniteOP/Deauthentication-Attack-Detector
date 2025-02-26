#!/usr/bin/env python

'''
This tool will help in detecting any Deauthentication attacks on the network.
By analyzing the output packet count, one can detect whether it falls under a DoS attack or if it is the normal behavior of the network.
'''

from scapy.all import *
from scapy.layers import Dot11

# get Network Interface from user
interface = raw_input('Enter your Network Interface: ')

# set Packet Counter
Packet_Counter = 1

# extract info of the packet
def info(packet):
    if packet.haslayer(Dot11):
        # The packet.subtype==12 statement indicates the deauthentication frame
        if ((packet.type == 0) & (packet.subtype==12)):
            global Packet_Counter
            print ("[+] Deauthentication Packet detected! ", Packet_Counter)
            Packet_Counter = Packet_Counter + 1
# Start Sniffing and Detecting Deauthentication Packets
sniff(iface=interface,prn=info)
