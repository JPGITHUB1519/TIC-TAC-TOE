import pygame

pygame.init()

class Piece(pygame.sprite.Sprite) :

	def __init__(self,x,y) :
		self.imagen_x = pygame.image.load("images/x.png")
		self.imagen_o = pygame.image.load("images/o.png")
		self.imagen_transparente = pygame.image.load("images/fondo_transparente.png")
		self.type_piece = ""
		self.image = self.imagen_transparente
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = x,y

	def update(self, pantalla) :

		pantalla.blit(self.image, self.rect)

class Cursor(pygame.Rect) :

	def __init__(self) :

		pygame.Rect.__init__(self,0,0,0,1)

	def update(self, pantalla) :

		self.left, self.top = pygame.mouse.get_pos()


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

	cursor1 = Cursor()
	piece1 = Piece(110,110)
	piece2 = Piece(110,110)
	reloj = pygame.time.Clock()
	salir = False


	while salir != True :

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :

				salir = True

		reloj.tick(20)
		pantalla.fill((255,255,255))

		cursor1.update(pantalla)

		if cursor1.colliderect(piece1.rect) :

			piece1.image = piece1.imagen_x
		draw_lines(pantalla)
		piece1.update(pantalla)
		#y1.update(pantalla)
		pygame.display.update()


	pygame.quit()

main()
