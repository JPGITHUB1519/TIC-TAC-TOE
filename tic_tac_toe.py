import pygame

pygame.init()

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
		pygame.display.update()

	pygame.quit()

main()
