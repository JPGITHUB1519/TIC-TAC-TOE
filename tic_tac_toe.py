import pygame

pygame.init()

def draw_lines(pantalla) :

	x = 200
	yinicio = 100
	yfinal = 400 

	for i in range(0,2) :

		pygame.draw.line(pantalla, (0,0,0),(x,yinicio),(x,yfinal),1)
		x += 100

	xyfinal = 200
	for i in range(0,2) :

		pygame.draw.line(pantalla, (0,0,0),(100,xyfinal),(400,xyfinal),1)
		xyfinal += 100
		

def main() :

	pygame.init()

	pantalla = pygame.display.set_mode([700,500])

	reloj = pygame.time.Clock()
	salir = False

	while salir != True :

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :

				salir = True

		reloj.tick(20)
		pantalla.fill((255,255,255))

		draw_lines(pantalla)
		pygame.display.update()

	pygame.quit()

main()
