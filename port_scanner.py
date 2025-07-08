import argparse
import socket
from datetime import datetime

def scan_ports(target, start_port=1, end_port=1024):
    print(f"\nScanning Target: {target}")
    print(f"Scanning started at: {datetime.now()}")
    print("-" * 50)

    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port} is open")
    except KeyboardInterrupt:
        print("\nScan cancelled by user.")
    except socket.gaierror:
        print("\nError: Hostname could not be resolved.")
    except socket.error:
        print("\nError: Could not connect to server.")

    print("-" * 50)
    print(f"Scan completed at: {datetime.now()}")
    print("-" * 50)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("host", nargs='?', default='localhost', help="Target IP address or domain to scan (default: localhost)")

    parser.add_argument("--start", type=int, default=1, help="Start port (default=1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default=1024)")
    
    args = parser.parse_args()
    target_ip = socket.gethostbyname(args.host)

    scan_ports(target_ip, args.start, args.end)
