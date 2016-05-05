import pygame

pygame.init()

class Piece(pygame.sprite.Sprite) :

	def __init__(self, imagen, type_piece,x,y) :

		self.type_piece = type_piece
		self.imagen_normal = imagen
		self.imagen_oculta = pygame.image.load("images/fondo_transparente.png")
		self.image = self.imagen_normal
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = x,y

	def update(self, pantalla) :

		pantalla.blit(self.image, self.rect)


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
	imagen_x = pygame.image.load("images/x.png")
	imagen_o = pygame.image.load("images/o.png")

	x1 = Piece(imagen_x,"x",110,110)
	y1 = Piece(imagen_o,"0",110,110)
	reloj = pygame.time.Clock()
	salir = False


	while salir != True :

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :

				salir = True

		reloj.tick(20)
		pantalla.fill((255,255,255))

		draw_lines(pantalla)
		#x1.update(pantalla)
		y1.update(pantalla)
		pygame.display.update()


	pygame.quit()

main()
