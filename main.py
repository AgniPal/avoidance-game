import pygame
pygame.init()

# Создаём игровое окно
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My Game") # название окна
image = pygame.image.load("") # путь к изображению (к спрайту)
image.rect = image.get_rect() # хитбокс изображения (рамка вокруг изображения)

speed = 5 # скорость перемещения изображения

# Запускаем игру
run = True
while run:
    for event in pygame.event.get(): # обрабатываем события: event = событие, pygame.event.get() = список событий
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION: # управление изображением через мышку
            mouseX, mouseY = pygame.mouse.get_pos
            image.rect.x = mouseX - (image.get_width() / 2)
            image.rect.y = mouseY - (image.get_height() / 2)

 #   # Управление изображением с клавиатуры
 #   keys = pygame.key.get_pressed()
 #   if keys[pygame.K_LEFT]: # нажатие левой стрелки
 #       image.rect.x -= speed
 #   if keys[pygame.K_RIGHT]: # нажатие правой стрелки
 #       image.rect.x += speed
 #   if keys[pygame.K_UP]: # нажатие верхней стрелки
 #       image.rect.y -= speed
 #   if keys[pygame.K_DOWN]: # нажатие нижней стрелки
 #       image.rect.y += speed

    # Отрисовка экрана
    screen.fill((0, 0, 0)) # придание цвета экрану
    screen.blit(image, image.rect) # отрисовка изоражения
    pygame.display.update() # обновление экрана (вместо update можно использовать flip)

pygame.quit()
