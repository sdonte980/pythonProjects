
import socket
import sys
from typing import Dict, List

def getArg():
    if (len(sys.argv) < 2) :
     print('Usage : python parentServer.py [myPort] [parentIP] [parentPort] [parentFileName]')
     sys.exit()
    myPort = int(sys.argv[1])
    ParentIP = sys.argv[2]
    parentPort = int(sys.argv[3])
    parentFileName = sys.argv[4]
    return myPort, ParentIP, parentPort, parentFileName


def readFile(filepath):
    f = open( filepath, 'r',  encoding='utf-8' )
    all_lines = f.readlines()
    f.close()
    return all_lines


def writeFile(filepath, line):
    f = open( filepath, 'a',  encoding='utf-8')
    f.writelines( line + str( "\n" ) )
    f.close()


def orderData(d_list):
    orderList = []
    for line in d_list:
        orderList.append( dict( zip( line.split( ',' ), line.split() ) ) )
    # print(out)
    return orderList


def findValue(orderList, key):
    for i in range(len(orderList)):
     for o in orderList[i]:
      if (o == key):
        return orderList[i].get(key)
      else:
        value = "usage: not find in the order list"
        continue
    return value

def seperateBfromKey(key):
    temp = key.split("'")
    return temp[1]

def getInternetAdress(value):
    internetAdress = value.split( ',' )
    return internetAdress[0]


def getIpAdress(value):
    ipAdress = value.split( ',' )
    return ipAdress[1]


def getTTL(value):
    TTL = value.split( ',' )
    return TTL[2]



myPort, ParentIP, parentPort, parentFileName = getArg()

d_list = readFile( parentFileName )
# d_list = readFile( filepath )
print( d_list )
orderList = orderData( d_list )

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
s.bind(('', myPort))
err_finding = "usage: not find in the order list"
while True:
    data, addr = s.recvfrom( 2024 )
    print( str( data ), addr )
    if data != 0:
        key1 = seperateBfromKey(str(data))
        value = findValue(orderList, key1)
        if((value) == (err_finding)):
            flags = 1
            data = bytes(value.encode("utf-8"))
            s.sendto(data, addr)
        # get_value = findValue( value )
        data = bytes(value.encode(encoding = "utf-8"))
        s.sendto(data, addr)
        print("sucsses sending")


#check_data_p = bytes(data.encode("utf-8"))
#p_s.sendto(check_data_p,(ParentIP, parentPort))


# filepath = "/home/alex/PycharmProjects/pythonProject1/venv/parent"

