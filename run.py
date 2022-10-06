from game.pygame_four_in_line import Game_four_in_line
import pygame

if __name__ == "__main__":
    pygame.init()
    games = Game_four_in_line()
    games.main()