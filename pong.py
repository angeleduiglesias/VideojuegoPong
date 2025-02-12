import pygame

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong en Python")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Variables de las paletas
PALETA_ANCHO, PALETA_ALTO = 15, 100
paleta_izq = pygame.Rect(20, ALTO // 2 - PALETA_ALTO // 2, PALETA_ANCHO, PALETA_ALTO)
paleta_der = pygame.Rect(ANCHO - 35, ALTO // 2 - PALETA_ALTO // 2, PALETA_ANCHO, PALETA_ALTO)

# Pelota
PELOTA_TAM = 15
pelota = pygame.Rect(ANCHO // 2, ALTO // 2, PELOTA_TAM, PELOTA_TAM)
vel_x, vel_y = 5, 5

# Velocidad de las paletas
vel_paleta = 7

# Bucle principal
ejecutando = True
while ejecutando:
    pygame.time.delay(20)  # Control de velocidad
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Movimiento de las paletas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta_izq.top > 0:
        paleta_izq.y -= vel_paleta
    if teclas[pygame.K_s] and paleta_izq.bottom < ALTO:
        paleta_izq.y += vel_paleta
    if teclas[pygame.K_UP] and paleta_der.top > 0:
        paleta_der.y -= vel_paleta
    if teclas[pygame.K_DOWN] and paleta_der.bottom < ALTO:
        paleta_der.y += vel_paleta

    # Movimiento de la pelota
    pelota.x += vel_x
    pelota.y += vel_y

    # Rebote en los bordes superior e inferior
    if pelota.top <= 0 or pelota.bottom >= ALTO:
        vel_y *= -1

    # Rebote en las paletas
    if pelota.colliderect(paleta_izq) or pelota.colliderect(paleta_der):
        vel_x *= -1

    # Reinicio si la pelota sale de la pantalla
    if pelota.left <= 0 or pelota.right >= ANCHO:
        pelota.x, pelota.y = ANCHO // 2, ALTO // 2
        vel_x *= -1  # Cambiar dirección después de un punto

    # Dibujar en la pantalla
    VENTANA.fill(NEGRO)
    pygame.draw.rect(VENTANA, BLANCO, paleta_izq)
    pygame.draw.rect(VENTANA, BLANCO, paleta_der)
    pygame.draw.ellipse(VENTANA, BLANCO, pelota)
    pygame.draw.aaline(VENTANA, BLANCO, (ANCHO // 2, 0), (ANCHO // 2, ALTO))

    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()
