#!/usr/bin/env python
#
#
#
### IMPORT ###
import getopt
import logging
import re
import string
import svs

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


from scapy.all import *




### /IMPORTS ###

def usage():
    print "Packet Parser for Network Mapping"
    print "---------------------------------"
    print ""
    print "Parses PCAP or Live network traffic"
    print "Parses CDP, 802.1D (STP etc), ARP, RARP"
    print "Dumps information into database for parsing into a network map"



def parse_packets(pkts):
    
    for p in pkts:
        


