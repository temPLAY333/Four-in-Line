import unittest
from unittest.mock import patch
import pygame
from pygame_four_in_line import Game_four_in_line

@patch('pygame.display.update')
@patch('pygame.display.flip')
@patch('pygame.draw.circle')

class Test_four_in_line(unittest.TestCase):
    
    def test_00_display(self,*args):
        game = Game_four_in_line()
        self.assertIsNotNone(game.main())
    



if __name__ == "__main__":
    unittest.main()
