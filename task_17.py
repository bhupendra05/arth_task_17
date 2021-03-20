import socket
import threading
import os

os.system("clear")
def recieve(ip1,port1):
    s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((ip1,port1))
    while True :
        os.system("tput setaf 14")
        x = s.recvfrom(1020)
        data = x[0].decode()
        print("\t\t\t\t\t Friend " + data)
def send(ip2,port2):
    k=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True :
        os.system("tput setaf 47")
        p = input()
        data=p.encode()
        x = k.sendto(data,(ip2,port2))
os.system("tput setaf 6")
ip1= input("Enter Your System IP :- ")
p1=input("Enter your System Port NO. :- ")
port1= int(p1)

os.system("tput setaf 9")
ip2= input("Enter Friend System  IP :- ")
p2=input("Enter Friend System Port NO. :- ")
port2= int(p2)
os.system("clear")
os.system("tput setaf 10")

print("............................................... welcome to UDP Chat Server..............................")
print("********************************************************************************************************")
x1 = threading.Thread(target=recieve , args=(ip1,port1))
x2 = threading.Thread(target=send , args=(ip2,port2))

x1.start()
x2.start()
