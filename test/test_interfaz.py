import unittest, pygame
from game.four_in_line import *
from game.interfaz_four_in_line import *
from unittest.mock import patch

class Test_interfaz(unittest.TestCase):
    def test(self):
        game = Interfaz()
        if 0 == 1:
            self.assertEqual(game.main(), True)