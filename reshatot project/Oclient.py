import socket
import sys

if (len(sys.argv) < 2) :
    print('Usage : python client.py [serverIP] [serverPort]')
    sys.exit()
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
 print("enter internet adress:")
 internetAdress = input()
 if internetAdress == "exit":
    print("the system is close")
    s.close()
    sys.exit()
 internetAdress = bytes(internetAdress.encode("utf-8"))
 s.sendto(internetAdress,(serverIP, serverPort))

 data, addr = s.recvfrom( 1024 )
 print(data.decode(encoding="utf-8"),addr)

s.close()
