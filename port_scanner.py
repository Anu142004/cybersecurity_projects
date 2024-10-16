import socket
from datetime import datetime

# Function to scan a single port
def scan_port(ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Set timeout for socket connection
        
        # Try to connect to the IP and port
        result = sock.connect_ex((ip, port))  # Returns 0 if port is open
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        sock.close()  # Close the socket after scanning
    except Exception as e:
        print(f"Error: {e}")
        return

# Function to scan multiple ports
def scan_ports(ip, start_port, end_port):
    print(f"Starting scan on {ip} from port {start_port} to {end_port}")
    start_time = datetime.now()  # Start time for performance tracking

    # Loop through a range of ports
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)
    
    end_time = datetime.now()  # End time for performance tracking
    print(f"Scan completed in: {end_time - start_time}")

# Main function to execute the port scan
if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    scan_ports(target_ip, start_port, end_port)
