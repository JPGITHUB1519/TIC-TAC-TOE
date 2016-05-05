import pygame
import sys

pygame.init()

class Piece(pygame.sprite.Sprite) :

	def __init__(self,x,y,pos) :
		self.imagen_x = pygame.image.load("images/x.png")
		self.imagen_o = pygame.image.load("images/o.png")
		self.imagen_transparente = pygame.image.load("images/fondo_transparente.png")
		self.type_piece = ""
		self.played = False
		self.pos = pos
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

def play(cursor, pieza, jugador1, jugador2, game_result, turnos) :

	if cursor.colliderect(pieza.rect) :

		if jugador1.turno == True  and pieza.played == False:

			pieza.image = pieza.imagen_o
			pieza.type_piece = "o"
			jugador1.turno = False
			jugador2.turno = True
			pieza.played = True
			game_result[pieza.pos[0]][pieza.pos[1]] = pieza.type_piece
			turnos += 1
			

		if jugador2.turno == True  and pieza.played == False:

			pieza.image = pieza.imagen_x
			pieza.type_piece = "x"
			jugador1.turno = True
			jugador2.turno = False
			pieza.played = True
			game_result[pieza.pos[0]][pieza.pos[1]] = pieza.type_piece
			turnos += 1
	
	return turnos

def check_structure(game_result) :

	# horinzontally

	for x in range(0,3) :

		if (game_result[x][0] == game_result[x][1] == game_result[x][2]) and game_result[x][0] != "." :

			return game_result[x][0]

	# vertically

	for x in range(0,3) :

		if (game_result[0][x] == game_result[1][x] == game_result[2][x]) and game_result[0][x] != "." :

			return game_result[0][x]

	# diagonally

	# principal diagonal

	if(game_result[0][0] == game_result[1][1] == game_result[2][2]) and game_result[0][0] != "." :

		return game_result[0][0]

	#check secundary diagonal
	if(game_result[0][2] == game_result[1][1] == game_result[2][0]) and game_result[0][2] != "." :
		
		return game_result[0][2]

	# else return draw
	return "."

class Boton(pygame.sprite.Sprite) :

	def __init__(self, imagen1, imagen2, x = 200, y = 200) :

		self.imagen_normal = imagen1
		self.imagen_seleccion = imagen2
		self.rect = self.imagen_normal.get_rect()
		self.rect.left, self.rect.top = x,y 
		self.imagen_actual = self.imagen_normal

	def update(self, pantalla, cursor) :

		if cursor.colliderect(self.rect) :

			self.imagen_actual = self.imagen_normal

		else :

			self.imagen_actual = self.imagen_seleccion

		pantalla.blit(self.imagen_actual, self.rect)


def check_winner(game_result, turnos) :

	winner = check_structure(game_result)

	if winner != "." :

		return winner

	if turnos == 9 :

		if winner == "." :

			return winner

	return "none"

def show_menu(pantalla,cursor,botones) :

	for button in botones :

		button.update(pantalla, cursor)

	fuente1 = pygame.font.Font("fonts/Pacifico.ttf",30)

	#texto_titulo = fuente1.render("TIC TAC TOE GAME",0,(0,0,255))

	#pantalla.blit(texto_titulo, (50,35))

	image_title = pygame.image.load("images/tic_logo.jpg")

	pantalla.blit(image_title, (75,150))

	cursor.update(pantalla)

def main() :

	pygame.init()

	pantalla = pygame.display.set_mode([500,600])

	cursor1 = Cursor()

	# Pieces
	xpiece = 110
	piece1 = Piece(110,110,[0,0])
	piece2 = Piece(215,110,[0,1])
	piece3 = Piece(310,110,[0,2])
	piece4 = Piece(110,210,[1,0])
	piece5 = Piece(215,210,[1,1])
	piece6 = Piece(310,210,[1,2])
	piece7 = Piece(110,310,[2,0])
	piece8 = Piece(215,310,[2,1])
	piece9 = Piece(310,310,[2,2])

	# Players

	player1 = Jugador("Jean")
	player2 = Jugador("Anonimo")

	player1.turno = True

	reloj = pygame.time.Clock()
	salir = False

	# data structure of the game

	game_result = [[".",".","."],[".",".","."],[".",".","."]]

	# aux

	winner = ""
	turnos = 0

	# fuentes

	fuente_atarian = pygame.font.Font("fonts/atarian.ttf", 35)
	fuente_atarian2 = pygame.font.Font("fonts/atarian.ttf", 60)
	texto_jugador1 = fuente_atarian.render("Jugador 1 :" + player1.nombre, 0,(0,0,255))
	texto_jugador2 = fuente_atarian.render("Jugador 2: " + player2.nombre, 0,(0,0,255))
	text_play_again = fuente_atarian.render("Pulsa Espacio Para Jugar...",0,(0,0,255))
	#images 
	imagen_boton_jugar = pygame.image.load("images/jugar.png")
	imagen_boton_jugar_hover = pygame.image.load("images/jugar_hover.png")
	imagen_boton_salir = pygame.image.load("images/salir.png")
	imagen_boton_salir_hover = pygame.image.load("images/salir_hover.png")
	boton1 = Boton(imagen_boton_jugar, imagen_boton_jugar_hover, 100,400)
	boton2 = Boton(imagen_boton_salir, imagen_boton_salir_hover,300,400)
	#conds scenes
	cond_menu = True
	cond_game = False
	cond_gameover = False


	while salir != True :

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :

				salir = True
			
			if event.type == pygame.MOUSEBUTTONDOWN :

				# if click and collide with the background
				if winner == "none" :
					turnos = play(cursor1, piece1, player1, player2, game_result, turnos)
					turnos = play(cursor1, piece2, player1, player2, game_result, turnos)
					turnos = play(cursor1, piece3, player1, player2, game_result, turnos)
					turnos = play(cursor1, piece4, player1, player2, game_result, turnos)
					turnos = play(cursor1, piece5, player1, player2, game_result, turnos)
					turnos = play(cursor1, piece6, player1, player2, game_result, turnos)
					turnos = play(cursor1, piece7, player1, player2, game_result, turnos)
					turnos = play(cursor1, piece8, player1, player2, game_result, turnos)
					turnos = play(cursor1, piece9, player1, player2, game_result, turnos)

				if cond_menu == True :

					if cursor1.colliderect(boton1.rect) :

						cond_game = True
						cond_menu = False
					if cursor1.colliderect(boton2) :

						pygame.quit()
						# salir del programa
						sys.exit(0)

			# play again option
			if event.type == pygame.KEYDOWN :
				
				if event.key == pygame.K_SPACE :
					
					if cond_gameover == True :

						cond_gameover = False
						piece1.image = piece1.imagen_transparente
						piece1.played = False
						piece2.image = piece2.imagen_transparente
						piece2.played = False
						piece3.image = piece3.imagen_transparente
						piece3.played = False
						piece4.image = piece4.imagen_transparente
						piece4.played = False
						piece5.image = piece5.imagen_transparente
						piece5.played = False
						piece6.image = piece6.imagen_transparente
						piece6.played = False
						piece7.image = piece7.imagen_transparente
						piece7.played = False
						piece8.image = piece8.imagen_transparente
						piece8.played = False
						piece9.image = piece9.imagen_transparente
						piece9.played = False

						game_result = [[".",".","."],[".",".","."],[".",".","."]]
						turnos = 0
						winner = "none"
						player1.turno = True
						player2.turno = False

		reloj.tick(20)
		pantalla.fill((255,255,255))

		if cond_menu == True :

			show_menu(pantalla, cursor1, [boton1, boton2])

		if cond_game == True :
			cursor1.update(pantalla)
			draw_lines(pantalla)
			pantalla.blit(texto_jugador1,(50,445))
			pantalla.blit(texto_jugador2,(270,445))

			piece1.update(pantalla)
			piece2.update(pantalla)
			piece3.update(pantalla)
			piece4.update(pantalla)
			piece5.update(pantalla)
			piece6.update(pantalla)
			piece7.update(pantalla)
			piece8.update(pantalla)
			piece9.update(pantalla)

			# check the game result to see if there is a winner
			winner = check_winner(game_result, turnos)

			if winner != "none" :

				if winner == "o" :

					texto_ganador = fuente_atarian2.render("Ganador : Jugador 1",0,(255,0,0))
					pantalla.blit(texto_ganador,(50,500))
				if winner == "x" :

					texto_ganador = fuente_atarian2.render("Ganador : Jugador 2", 0,(255,0,0))
					pantalla.blit(texto_ganador,(45,500))
				if winner == "." :

					texto_ganador = fuente_atarian2.render("Empate", 0,(255,0,0))
					pantalla.blit(texto_ganador,(175,500))

				pantalla.blit(text_play_again,(100,20))
				cond_gameover = True

		
		pygame.display.update()

		

	pygame.quit()

main()
