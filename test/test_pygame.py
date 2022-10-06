import sys
sys.path.append('C:\\Users\\Admin\\Documents\\PythonCodigos\\Computacion\\4_en_Linea\\game')
import unittest
from four_in_line import *
from unittest.mock import patch
import pygame

@patch('pygame.display.update')
@patch('pygame.display.flip')
@patch('pygame.draw.circle')

class Test_four_in_line(unittest.TestCase):
    pass



if __name__ == "__main__":
    unittest.main()
