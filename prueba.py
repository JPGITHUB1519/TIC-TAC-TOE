import pygame

pygame.init()

def draw_lines(pantalla) :

	
	pygame.draw.line(pantalla, (0,0,0),(10,10),(200,10),1)


def main() :

	pygame.init()

	pantalla = pygame.display.set_mode([500,500])

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
