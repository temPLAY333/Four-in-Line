import unittest, pygame
from game.four_in_line import *
from unittest.mock import patch

@patch('pygame.display.update')
@patch('pygame.display.flip')
@patch('pygame.draw.circle')

class Test_four_in_line(unittest.TestCase):
    pass



# if __name__ == "__main__":
#     unittest.main()
