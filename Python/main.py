import pygame
from game import Game
from constants import *

if __name__ == "__main__":
    pygame.init()

    # Tạo cửa sổ
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Khởi tạo tiến trình game
    game = Game()

    # Chạy game
    game.run(screen)

    # Thoát game
    pygame.quit()