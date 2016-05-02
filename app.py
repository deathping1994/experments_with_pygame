import pygame
import socket
import select

# import pdb

def main():
	
	pygame.init()
	sock=socket.socket()
	sock.bind(('localhost',8002))
	sock.listen(5)
	clock=pygame.time.Clock()
	screen = pygame.display.set_mode((400, 300))
	done = False
	x=0
	y=0
	flow=3
	ycord=40
	t=1
	pygame.draw.rect(screen, (120,120,120), pygame.Rect(0, 0, 30, 10))
	pygame.draw.rect(screen, (120,120,120), pygame.Rect(10, 10, 10, 10))
	pygame.draw.rect(screen, (120,120,120), pygame.Rect(0, 25, 10, 8))
	pygame.draw.circle(screen,(120,120,120),(15,25),10)
	pygame.draw.rect(screen, (120,120,120), pygame.Rect(20, 25, 18, 8))
	pygame.draw.rect(screen, (120,120,120), pygame.Rect(30, 25, 8, 18))
	sock.listen(5)
	c,addr=sock.accept()
	# socklist=[]
	# socklist.append(c)
	print ""
	print "client connected"
	temp=c.recv(1)
	flow=int(temp)

	while not done:
		# readsock,writesock,err=select.select(socklist,[],[])
		# for te in readsock:
					# temp=2
		y=0.5*9.8*t*t
		if flow==1:
			t=1
			pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, ycord-y, 10, 10))
			pygame.draw.rect(screen, (10,10,255), pygame.Rect(30, ycord, 10, 10))
		elif flow==2:
			t=2
			pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, ycord-y, 10, 10))
			pygame.draw.rect(screen, (10,10,255), pygame.Rect(30, ycord, 10, 10))
		elif flow==3:
			t=4
			pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, ycord-y, 10, 20))
			pygame.draw.rect(screen, (10,10,255), pygame.Rect(30, ycord, 10, 20))
		print y
		ycord+=y
		if ycord>300:
			pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, ycord, 10, 10))
			ycord=40
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					done = True		
		pygame.display.flip()
		clock.tick(60)
if __name__ == '__main__':
	main()