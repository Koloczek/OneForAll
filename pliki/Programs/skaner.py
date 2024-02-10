import ipaddress
import threading
import subprocess

class scanner:
    def run(self):
        def ping_host(ip, available_hosts, timeout=2):
            try:
                result = subprocess.check_output(['ping', '-c', '1', '-W', str(timeout), ip], stderr=subprocess.STDOUT, universal_newlines=True)
                if "1 packets transmitted, 1 received" in result and "0% packet loss" in result:
                    available_hosts.append(ip)
            except subprocess.CalledProcessError:
                pass
            
        def scan_ip_range(ip_range):
            try:
                network = ipaddress.IPv4Network(ip_range, strict=False)
            except ValueError:
                print("Niepoprawny zakres adresów IP.")
                return
    
            available_hosts = []
            threads = []
            for ip in network.hosts():
                ip = str(ip)
                thread = threading.Thread(target=ping_host, args=(ip, available_hosts))
                threads.append(thread)
                thread.start()
    
            for thread in threads:
                thread.join()
    
            if available_hosts:
                print("Dostępne hosty:")
                for host in available_hosts:
                    print(host)
            else:
                print("Brak dostępnych hostów w podanym zakresie.")
    

        ip_range = input("Podaj zakres adresów IP (np. 192.168.1.1/24): ")
        scan_ip_range(ip_range)
    
        input("Naciśnij Enter, aby kontynuować")
    