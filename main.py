import pygame
pygame.init()

# Создаём игровое окно
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My Game")

# Запускаем игру
run = True
while run:
    for event in pygame.event.get(): # обрабатываем события: event = событие, pygame.event.get() = список событий
        if event.type == pygame.QUIT:
            run = False

    # Придание цвета экрану
    screen.fill((0, 0, 0))
    pygame.display.update() # обновление экрана

pygame.quit()