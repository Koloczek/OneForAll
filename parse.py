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
   
    s = socket.socket(socket.AF_POCKET, socket.SOCK_RAW, socket.ntohs(3))
    
    while True:
        
        raw_data, addr = s.recvfrom(65535)
        eth = ethernet_head(raw_data)
        print('\nEthernet Frame: ')
        print('Destination: {}, Source: {}, Protocol: {}'.format(eth[0], eth[1], eth[2]))
        
        if eth[2] == 8:
            ipv4 = ipv4_head(eth[4])
            print( '\t - ' + 'IPv4 Packet:')
            print('\t\t - ' + 'Version: {}, Header Length: {}, TTL:{},'.format(ipv4[1], ipv4[2], ipv4[3]))
            print('\t\t - ' + 'Protocol: {}, Source: {}, Target:{}'.format(ipv4[4], ipv4[5], ipv4[6]))
        
            if ipv4[4] == 6:
                tcp = tcp_head(ipv4[7])
                print('\t -' + 'TCP Segment:')
                print('\t\t -' + 'Source Port: {}, Destination Port: {}'.format(tcp[0], tcp[1]))
                print('\t\t -' + 'Sequence: {}, Acknowledgment: {}'.format(tcp[2], tcp[3]))
                print('\t\t -' + 'Flags:')
                print('\t\t\t -' + 'URG: {}, ACK: {}, PSH:{}'.format(tcp[4], tcp[5], tcp[6]))
                print('\t\t\t -' + 'RST: {}, SYN: {}, FIN:{}'.format(tcp[7], tcp[8], tcp[9]))
                if len(tcp[10]) > 0:
                    #HTTP
                    if tcp[0] == 80 or tcp[1] == 80:
                        print('\t\t -' + 'HTTP Data: ')
                            try:
                             http = HTTP(tcp[10])
                             http_info = str(http[10]).split('\n')
                            for line in http_info:
                            print(DATA_TAB_3 + str(line))
                            except:
                            print(format_multi_line(DATA_TAB_3, tcp[10]))
                            else:
                                print(TAB_2 + 'TCP Data:')
                                print(format_multi_line(DATA_TAB_3, tcp[10]))

                            


main()

def ipv4_head(raw_data):
    version_header_lenght = raw_data[0]
    version = version_header_lenght >> 4
    header_lenght = (version_header_lenght & 15) * 4
    ttl, proto, src, target = Struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])
    data = raw_data[header_lenght:]
    src = get_ip(src)
    target = get_ip(target)
    return version, header_lenght, ttl, proto, src, target, data

def get_ip(addr):
    return '.'.join(map(str, addr))

def tcp_head(raw_data):
    (src_port, dest_port, sequence, acknowledgment, offset_reserved_flags) = Struct.unpack('! H H L L H', raw_data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    data = raw_data[offset:]
    return src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data
