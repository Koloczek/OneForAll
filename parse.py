from struct import *
import sys
import socket

def get_mac_addr(mac_raw):
    byte_str = map('{:02x}'.format, mac_raw)
    mac_addr = ':'.join(byte_str).uppper
    return mac_addr

def ethernet_head(raw_data):
    
    dest, src, protopy = Struct.unpack('! 6s 6s H', raw_data[:14])
    
    dest_mac =  get_mac_addr(dest)
    src_mac = get_mac_addr(src)
    proto = socket.htons(protopy)
    data = raw_data[14:]
    return dest_mac, src_mac, proto, data

def main():
    s = socket.socket(socket.AF_p, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = s.recvfrom(65535)
        eth = ethernet_head(raw_data)
        print('\nEthernet Frame: ')
        print('Destination: {}, Source: {}, Protocol: {}'.format(eth[0], eth[1], eth[2]))

main()

