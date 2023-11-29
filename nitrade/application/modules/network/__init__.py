import socket
import psutil
import requests
from application.packages.error_handling import ErrorHandling


class Network:
    def __init__(self):
        self.get_ip_address()
        self.get_network_interface()
        self.get_network_statistics()

    def get_ip_address(self):
        try:
            response = requests.get('https://httpbin.org/ip')
            response.raise_for_status()
            public_ip = response.json()['origin']

            api_url = f"http://ipinfo.io/{public_ip}/json"
            response = requests.get(api_url)
            response.raise_for_status()

            host_name = socket.gethostname()
            ip_address = socket.gethostbyname(host_name)

            print("\n[+] IP address:")
            print("    [-] Host name :", host_name)
            print("    [-] Local IP address :", ip_address)
            print("    [-] Public IP address :", public_ip)

            ip_info = response.json()
            print("\n[+] Information for the IP address:")
            print(f"    [-] IP :", ip_info['ip'])
            print(f"    [-] City :", ip_info['city'])
            print(f"    [-] Region :", ip_info['region'])
            print(f"    [-] Country :", ip_info['country'])
            print(f"    [-] geographic coordinates :", ip_info['loc'])
            print(f"    [-] Internet Service Provider (ISP) :", ip_info['org'])

        except requests.RequestException as error:
            ErrorHandling.output("401", error)

    def get_network_interface(self):
        network_interfaces = psutil.net_if_addrs()
        print("\n[+] Network Interfaces:")
        for interface, addresses in network_interfaces.items():
            print("    [+] Interface :", interface)
            for address in addresses:
                print("        [-] Address :", address.address)
                print("        [-] Netmask :", address.netmask)
                print("        [-] Broadcast :", address.broadcast)

    def get_network_statistics(self):
        network_stats = psutil.net_io_counters()
        print("\n[+] Network Statistics:")
        print("    [-] Bytes sent:", network_stats.bytes_sent)
        print("    [-] Bytes received:", network_stats.bytes_recv, "\n")
