import socket

# Target IP: Localhost for testing or any specific IP
target = "127.0.0.1" 

print(f"--- Automated Port Scanner Started on: {target} ---")

def port_scan(port):
    try:
        # Creating a socket for TCP connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Fast timeout for efficiency as per resume
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()
    except Exception as e:
        pass

# Scanning ports 1-100 (Reconnaissance Phase)
print("Scanning ports 1 to 100...")
for port in range(1, 101):
    port_scan(port)

print("Scan Complete.")