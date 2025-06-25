import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Base - Pygame")

BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
GRIS = (200, 200, 200)
NEGRO = (0, 0, 0)

jugador = pygame.Rect(50, 150, 50, 50)
velocidad_jugador = 5
enemigo = pygame.Rect(ANCHO, random.randint(0, ALTO - 50), 50, 50)
velocidad_enemigo = 3

fuente = pygame.font.SysFont(None, 36)
puntos = 0
tiempo_segundos = 0

reloj = pygame.time.Clock()

# Carga sonidos (archivos .wav u .ogg en la carpeta)
sonido_punto = pygame.mixer.Sound('punto.wav')
sonido_colision = pygame.mixer.Sound('colision.wav')

# Variables de estado
jugador_color = AZUL
juego_activo = False
tiempo_evento = pygame.USEREVENT + 1
pygame.time.set_timer(tiempo_evento, 1000)  # Evento cada 1 segundo para contar tiempo

def mostrar_texto(texto, x, y, color=NEGRO):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

def menu_inicio():
    pantalla.fill(GRIS)
    mostrar_texto("Presiona ESPACIO para iniciar", 120, ALTO//2 - 20)
    pygame.display.update()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == tiempo_evento and juego_activo:
            tiempo_segundos += 1
        if evento.type == pygame.KEYDOWN:
            if not juego_activo and evento.key == pygame.K_SPACE:
                # Reiniciar juego
                juego_activo = True
                puntos = 0
                tiempo_segundos = 0
                jugador_color = AZUL
                jugador.topleft = (50, 150)
                enemigo.left = ANCHO
                enemigo.top = random.randint(0, ALTO - 50)

    if not juego_activo:
        menu_inicio()
        continue

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and jugador.top > 0:
        jugador.move_ip(0, -velocidad_jugador)
    if teclas[pygame.K_DOWN] and jugador.bottom < ALTO:
        jugador.move_ip(0, velocidad_jugador)
    if teclas[pygame.K_LEFT] and jugador.left > 0:
        jugador.move_ip(-velocidad_jugador, 0)
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.move_ip(velocidad_jugador, 0)

    enemigo.move_ip(-velocidad_enemigo, 0)
    if enemigo.right < 0:
        enemigo.left = ANCHO
        enemigo.top = random.randint(0, ALTO - 50)
        puntos += 1
        sonido_punto.play()

    if jugador.colliderect(enemigo):
        jugador_color = ROJO
        sonido_colision.play()
        pygame.display.update()
        pygame.time.delay(1000)
        juego_activo = False  # Regresa al menú

    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, jugador_color, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    mostrar_texto(f"Puntos: {puntos}", 10, 10)
    mostrar_texto(f"Tiempo: {tiempo_segundos}s", 10, 40)

    pygame.display.update()
    reloj.tick(60)