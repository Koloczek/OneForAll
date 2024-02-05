import pyshark

class sniffer:
    def run(self):
        number_of_packets = int(input("Podaj czas w którym program ma przechwytywać pakiety (s): "))
        eth_interface = input("Podaj interface sieciowy na którym chcesz nasłuchiwać: ")
    
        # Przechwytywanie pakietów na żywo
        capture = pyshark.LiveCapture(interface=eth_interface)
        capture.sniff(timeout=number_of_packets)
        packets = [pkt for pkt in capture._packets]
        capture.close()
        for packet in packets:
            print("Nowy", packet)

        input("Naciśnij Enter, aby kontynuować")
    