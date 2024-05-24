import pygame
import random
import time

pygame.init()

# Размеры окна
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Watermelon Game")

# Классы
class Watermelon:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.lives = 5

    def update_position(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.rect.x = mouseX - self.rect.width // 2
        self.rect.y = mouseY - self.rect.height // 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Drop:
    def __init__(self, image_path, x, y, speed):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def update_position(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Game:
    def __init__(self, watermelon_image, drop_image, num_drops, drop_speed, game_time):
        self.watermelon = Watermelon(watermelon_image)
        self.drop_image = drop_image
        self.drops = []
        self.num_drops = num_drops
        self.drop_speed = drop_speed
        self.start_time = time.time()
        self.game_time = game_time
        self.running = True
        self.generate_drops()

    def generate_drops(self):
        for _ in range(self.num_drops):
            x = random.randint(0, window_size[0] - 50)
            y = random.randint(-100, -50)
            self.drops.append(Drop(self.drop_image, x, y, self.drop_speed))

    def update_drops(self):
        for drop in self.drops:
            drop.update_position()
            if drop.rect.top > window_size[1]:
                drop.rect.y = random.randint(-100, -50)
                drop.rect.x = random.randint(0, window_size[0] - 50)

    def check_collisions(self):
        for drop in self.drops:
            if self.watermelon.rect.colliderect(drop.rect):
                self.watermelon.lives -= 1
                drop.rect.y = random.randint(-100, -50)
                drop.rect.x = random.randint(0, window_size[0] - 50)
                if self.watermelon.lives <= 0:
                    self.running = False
                    print("Game Over! The watermelon is smashed.")
                    return

    def check_time(self):
        current_time = time.time()
        if current_time - self.start_time >= self.game_time:
            self.running = False
            print("You win! The watermelon survived.")

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.watermelon.update_position()
            self.update_drops()
            self.check_collisions()
            self.check_time()

            screen.fill((0, 0, 0))
            self.watermelon.draw(screen)
            for drop in self.drops:
                drop.draw(screen)
            pygame.display.update()

        pygame.quit()

# Запуск игры
watermelon_image = "img/watermelon.png"
drop_image = "img/drop2.png"
num_drops = 5  # Количество капель
drop_speed = 1  # Скорость капель
game_time = 30  # Время игры в секундах

game = Game(watermelon_image, drop_image, num_drops, drop_speed, game_time)
game.run()

