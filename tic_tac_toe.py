import pygame

pygame.init()

class Piece(pygame.sprite.Sprite) :

	def __init__(self,x,y) :
		self.imagen_x = pygame.image.load("images/x.png")
		self.imagen_o = pygame.image.load("images/o.png")
		self.imagen_transparente = pygame.image.load("images/fondo_transparente.png")
		self.type_piece = ""
		self.played = False
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

class Jugador() :

	def __init__(self, nombre) :

		self.turno = False
		self.nombre = nombre

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

def play(cursor, pieza, jugador1, jugador2) :

	if cursor.colliderect(pieza.rect) :

		if jugador1.turno == True  and pieza.played == False:

			pieza.image = pieza.imagen_o
			jugador1.turno = False
			jugador2.turno = True
			pieza.played = True

		if jugador2.turno == True  and pieza.played == False:

			pieza.image = pieza.imagen_x
			jugador1.turno = True
			jugador2.turno = False
			pieza.played = True

def check_structure(game_result) :

	# horinzontally

	for x in range(0,3) :

		if (game_result[x][0] == game_result[x][1] == game_result[x][2]) and game_result[x] != "." :

			return game_result[x][0]

	# vertically

	for x in range(0,3) :

		if (game_result[0][x] == game_result[1][x] == game_result[2][x]) and game_result[x] != "." :

			return game_result[0][x]

	# diagonally

	# principal diagonal

	if game_result[0][0] == "o" and game_result[1][1] == "o" and game_result[2][2] == "o" :

			return "o"

	if game_result[0][2] == "x" and game_result[1][1] == "x" and game_result[2][0] == "x" :

		return "x"

	# else return draw
	return "*"

def main() :

	pygame.init()

	pantalla = pygame.display.set_mode([700,500])

	cursor1 = Cursor()

	# Pieces
	xpiece = 110
	piece1 = Piece(110,110)
	piece2 = Piece(215,110)
	piece3 = Piece(310,110)
	piece4 = Piece(110,210)
	piece5 = Piece(215,210)
	piece6 = Piece(310,210)
	piece7 = Piece(110,310)
	piece8 = Piece(215,310)
	piece9 = Piece(310,310)

	# Players

	player1 = Jugador("Jean")
	player2 = Jugador("Anonimo")

	player1.turno = True

	reloj = pygame.time.Clock()
	salir = False

	# data structure of the game

	game = [[".",".","."],[".",".","."],[".",".","."]]

	while salir != True :

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :

				salir = True
			
			if event.type == pygame.MOUSEBUTTONDOWN :

				# if click and collide with the background
				play(cursor1, piece1, player1, player2)
				play(cursor1, piece2, player1, player2)
				play(cursor1, piece3, player1, player2)
				play(cursor1, piece4, player1, player2)
				play(cursor1, piece5, player1, player2)
				play(cursor1, piece6, player1, player2)
				play(cursor1, piece7, player1, player2)
				play(cursor1, piece8, player1, player2)
				play(cursor1, piece9, player1, player2)

		reloj.tick(20)
		pantalla.fill((255,255,255))

		cursor1.update(pantalla)

		draw_lines(pantalla)
		
		piece1.update(pantalla)
		piece2.update(pantalla)
		piece3.update(pantalla)
		piece4.update(pantalla)
		piece5.update(pantalla)
		piece6.update(pantalla)
		piece7.update(pantalla)
		piece8.update(pantalla)
		piece9.update(pantalla)
		pygame.display.update()

	pygame.quit()

main()
