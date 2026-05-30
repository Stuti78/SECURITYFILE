import socket

def scan_ports(target, ports):
    print(f"\nScanning Target: {target}")
    print("-" * 40)

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
            else:
                print(f"[CLOSED] Port {port}")

            sock.close()

        except KeyboardInterrupt:
            print("\nScan Stopped.")
            break

        except socket.gaierror:
            print("Hostname could not be resolved.")
            break

        except socket.error:
            print("Server not responding.")
            break

target_host = input("Enter Target IP or Domain: ")

common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

scan_ports(target_host, common_ports)