import socket
import sys
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nothing = sys.argv[1]
sport = int(sys.argv[2])
lport = int(sys.argv[3])

if len(sys.argv) != 4:
    print("sorry ")
    print("enter command like this ")
    print("python3 <file_name> <ip_address you want to scan> <starting_port> <ending_port>")
    sys.exit()



try :
    ip_addr = socket.gethostbyname(nothing)

except socket.gaierror:
    print("something called name resolution error \n frankly i also don't know this error")
    sys.exit()
print("scanning ip_addr",format(ip_addr))


    
def scan_port(port):
    
    co = s.connect_ex((ip_addr,port))
    if not co:

        print("port number ",port," is open")

    s.close()


for port in range(sport, lport+1):
    thread = threading.Thread(target = scan_port, args = (port,))
    thread.start()

