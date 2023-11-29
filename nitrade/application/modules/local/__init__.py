import os
import psutil
import platform


class Local:
    """ Class to retrieve Local system information. """

    def __init__(self):
        self.os_info = os.uname() if os.name == 'posix' else platform.uname()

        self.get_computer_info()
        self.get_memory_info()
        self.get_disk_info()
        self.get_cpu_info()

    def get_computer_info(self):
        """ Displays information about the computer. """
        print("\n[+] Computer:")
        print(f"    [-] Operating system: {self.os_info.system}")
        print(f"    [-] Name: {self.os_info.node}")
        print(f"    [-] Release: {self.os_info.release}")
        print(f"    [-] Version: {self.os_info.version}")
        print(f"    [-] Machine: {self.os_info.machine}")

    def get_memory_info(self):
        """ Displays the memory information. """
        memory_info = psutil.virtual_memory()
        print("\n[+] Memory:")
        print(f"    [-] Total memory (Go): {memory_info.total / (2 ** 30):.2f}")
        print(f"    [-] Memory used (Go): {memory_info.used / (2 ** 30):.2f}")
        print(f"    [-] Available memory (Go): {memory_info.available / (2 ** 30):.2f}")

    def get_disk_info(self):
        """ Displays information about disks. """
        disk_partitions = psutil.disk_partitions()
        print("\n[+] Disks:")
        for partition in disk_partitions:
            print("\n    [+] Disk:")
            print(f"        [-] Device: {partition.device}")
            print(f"        [-] Mountpoint: {partition.mountpoint}")
            print(f"        [-] File system type: {partition.fstype}")

            disk_usage = psutil.disk_usage(partition.mountpoint)
            print(f"        [-] Total space (Go): {disk_usage.total / (2 ** 30):.2f}")
            print(f"        [-] Used space (Go): {disk_usage.used / (2 ** 30):.2f}")
            print(f"        [-] Free space (Go): {disk_usage.free / (2 ** 30):.2f}")

    def get_cpu_info(self):
        """ Displays information about the CPU. """
        cpu_info = platform.processor()
        cpu_freq = psutil.cpu_freq()
        print("\n[+] CPU:")
        print(f"    [-] CPU Model: {cpu_info}")
        print(f"    [-] CPU Frequency (MHz): {cpu_freq.max:.2f}")
        print(f"    [-] Physical Cores: {psutil.cpu_count(logical=False)}")
        print(f"    [-] Logical Cores: {psutil.cpu_count(logical=True)}\n")
