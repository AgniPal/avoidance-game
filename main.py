import pygame
pygame.init()
import time # библиотека для работы со временем (используем при столкновении, для вывода единичного сообщения)

# Создаём игровое окно
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My Game") # название окна

image = pygame.image.load("img/watermelon.png") # путь к изображению (к спрайту)
image_rect = image.get_rect() # хитбокс изображения (рамка вокруг изображения)

image2 = pygame.image.load("img/drop2.png") # путь к изображению (к спрайту)
image_rect2 = image2.get_rect() # хитбокс изображения (рамка вокруг изображения)


speed = 5 # скорость перемещения изображения

# Запускаем игру
run = True
while run:
    for event in pygame.event.get(): # обрабатываем события: event = событие, pygame.event.get() = список событий
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION: # управление изображением через мышку
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX - 40
            image_rect.y = mouseY - 40
# Функция столкновения между объектами
    if image_rect.colliderect(image_rect2):
        print("Бум!")
        time.sleep(1)

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
    screen.blit(image, image_rect) # отрисовка изоражения
    screen.blit(image2, image_rect2) # отрисовка изоражения2
    pygame.display.update() # обновление экрана (вместо update можно использовать flip)

pygame.quit()
