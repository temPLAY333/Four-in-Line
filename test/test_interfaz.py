import unittest, pygame
from game.four_in_line import *
from game.interfaz_four_in_line import *
from unittest.mock import patch

class Test_interfaz(unittest.TestCase):
    def test(self):
        game = Interfaz()
        self.assertEqual(game.main(0), True)