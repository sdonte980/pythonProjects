import signal
import socket
import sys
import threading
import time


def getArg():
    if (len( sys.argv ) < 2):
        print( 'Usage : python server.py [myPort] [parentIP] [parentPort] [ipsFileName]' )
        sys.exit()
    myPort = int( sys.argv[1] )
    ParentIP = sys.argv[2]
    parentPort = int( sys.argv[3] )
    ipsFileName = sys.argv[4]
    return myPort, ParentIP, parentPort, ipsFileName


def readFile(filepath):
    f = open( filepath, 'r', encoding='utf-8' )
    all_lines = f.readlines()
    f.close()
    return all_lines


def writeFile(filepath, line):
    f = open( filepath, 'a', encoding='utf-8' )
    f.writelines( line + str( "\n" ) )
    f.close()


def eraseLineFromFile(filepath, chosed_line):
    with open( filepath, "r+" ) as f:
        new_f = f.readlines()
        f.seek( 0 )
        for line in new_f:
            if chosed_line not in line:
                f.write( line )
        f.truncate()
    f.close()


def orderData(d_list):
    orderList = []
    for line in d_list:
        orderList.append( dict( zip( line.split( ',' ), line.split() ) ) )
    # print(out)
    return orderList


def getValue(orderList, key):
    for i in range( len( orderList ) ):
        for o in orderList[i]:
            if (o == key):
                return orderList[i].get( key )
            else:
                value = "usage: not find in the order list"
                continue
    return value


def seperateBfromKey(key):
    temp = key.split( "'" )
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



myPort, ParentIP, parentPort, ipsFileName = getArg()

d_list = readFile( ipsFileName )
print( d_list )
orderList = orderData( d_list )

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
s.bind( ('', myPort) )
p_s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
err_finding = "usage: not find in the order list"
flag = 0
t = time.time()
temp = []
# לעשות ערך ענק לשנות
while True:
    if flag > 0:
        if ((time.time()-t) >= float(getTTL(temp))):
            eraseLineFromFile( ipsFileName, temp )
            flag = 0
    data, addr = s.recvfrom( 1024 )
    if data != 0:
        if flag > 0:
            d_list = readFile( ipsFileName )
            orderList = orderData( d_list )
        key = seperateBfromKey( str( data ) )
        value = getValue( orderList, key )
        if flag > 0:
            if ((time.time()-t) >= float(getTTL(value))):
             eraseLineFromFile( ipsFileName, value )
             flag = 0
        if (value == err_finding):
            check_data_p = bytes( data )
            p_s.sendto( check_data_p, (ParentIP, parentPort) )
            data_p, addr_p = p_s.recvfrom( 1024 )
            check_data_p1 = data_p.decode( encoding="utf-8" )
            print( data_p.decode( encoding="utf-8" ) )
            if (check_data_p1 == err_finding):
                data_p = bytes( err_finding, encoding="utf-8" )
                s.sendto( data_p, addr )
            else:
                key = getInternetAdress( check_data_p1 )
                value = check_data_p1
                ttl = getTTL( value )
                print( "ttl" )
                print( float( ttl ) )
                get_ip_Address = getIpAdress( value )
                data = bytes( get_ip_Address, encoding="utf-8" )
                s.sendto( data, addr )
                writeFile( ipsFileName, value)
                print("file writed")
                # print(value)
                temp = value
                print(temp)
                if ((time.time()-t) >= float(ttl)):
                    eraseLineFromFile( ipsFileName, value )
                flag += 1


        else:
             get_ip_Address = getIpAdress( value )
             data = bytes( get_ip_Address, encoding="utf-8" )
             s.sendto( data, addr )
    # p_s.close()
