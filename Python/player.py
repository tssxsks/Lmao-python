import pygame
from constants import *  # Ensure you import necessary constants


class Player:
    def __init__(self, ship_type):
        self.ship_type = ship_type
        self.x = screen_width // 2
        self.y = screen_height - spaceship_height - 10
        self.speed = spaceship_speed
        self.bullets = []
        self.lives = lives
        self.can_shoot = True

        # Load player image based on ship type
        self.ship_type = ship_type
        if self.ship_type == "basic":
            self.health = 100
            self.damage = 10
            self.image = pygame.image.load("player_basic.png").convert_alpha()
        elif self.ship_type == "advanced":
            self.health = 150
            self.damage = 15
            self.image = pygame.image.load("player_advanced.png").convert_alpha()
        elif self.ship_type == "elite":
            self.health = 200
            self.damage = 20
            self.image = pygame.image.load("player_elite.png").convert_alpha()
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Load bullet image
        self.bullet_image = pygame.image.load("bullets.png").convert_alpha()
        self.bullet_width = self.bullet_image.get_width()
        self.bullet_height = self.bullet_image.get_height()

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.width:
            self.x += self.speed

    def shoot(self):
        if self.can_shoot:
            bullet = pygame.Rect(
                self.x + self.width // 2 - self.bullet_width // 2,
                self.y,
                self.bullet_width,
                self.bullet_height,
            )
            self.bullets.append(bullet)
            self.can_shoot = False  # Prevent further shooting until key is released

    def draw(self, screen):
        # Draw the player image
        screen.blit(self.image, (self.x, self.y))

        # Draw bullets using the bullet image
        for bullet in self.bullets:
            screen.blit(self.bullet_image, (bullet.x, bullet.y))

        # Draw health bar
        pygame.draw.rect(screen, green, (10, 50, self.health * 2, 20))

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.y -= bullet_speed
        self.bullets = [
            bullet for bullet in self.bullets if bullet.y > 0
        ]  # Remove off-screen bullets

    def lose_health(self):
        self.health -= damage_per_collision
        if self.health <= 0:
            self.lives -= 1
            self.health = max_health
            if self.lives <= 0:
                return True  # Player is out of lives
        return False  # Player is still alive