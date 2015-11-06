import socket
hostname = raw_input("enter stuff:")
hostIP = socket.getfqdn(hostname)
print hostIP