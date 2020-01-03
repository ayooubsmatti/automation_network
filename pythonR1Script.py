import getpass
import sys
import telnetlib

HOST = "192.168.62.136 "
user = raw_input("Enter Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("int loop 0\n")
tn.write("ip address 1.1.1.1 255.255.255.255 \n")
tn.write("router ospf 1 \n")
tn.write("network 0.0.0.0 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")


print tn.read_all()
