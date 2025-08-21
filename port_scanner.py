#!/usr/bin/env python3

import socket

def scan_ports(host, ports):
    print(f"Scanning {host}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        sock.close()

if __name__ == "__main__":
    target = input("Enter host to scan (e.g., 127.0.0.1): ")
    ports = [22, 80, 443, 8080]  # You can add more ports
    scan_ports(target, ports)