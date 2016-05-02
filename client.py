import socket

def main():
	sock=socket.socket()
	sock.connect(('localhost',8002))
	print ("Enter choices\n1. droplet\n2.medium\n3.high")
	while 1:
		k=raw_input()
		sock.send(k)

if __name__ == '__main__':
	main()