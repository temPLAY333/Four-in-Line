from distutils.command.build import build
import unittest, io
from game.four_in_line import *
from game.interfaz_four_in_line import *
from unittest.mock import patch

class Test_interfaz(unittest.TestCase):
    def setUp(self):
        self.game = Interfaz()
    
    @patch ("builtins.input", side_effect=["1", "2"])
    def test_00_choose_color(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.choose_color()
        self.assertEqual(self.game.game.player_1, 1)
        self.assertEqual(self.game.game.player_2, 2)
        
    @patch ("builtins.input", side_effect=["4", "3"])
    def test_01_choose_color(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.choose_color()
        self.assertEqual(self.game.game.player_1, 4)
        self.assertEqual(self.game.game.player_2, 3)
    
    @patch ("builtins.input", side_effect=["f", "0", "2", "2", "3"])
    def test_02_choose_color(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as output:
            self.game.choose_color()
        print_output = output.getvalue().split('\n')

        self.assertEqual(print_output[1], "Write a number, asshole")
        self.assertEqual(print_output[3], "Choose one of the options, asshole")
        self.assertEqual(print_output[6], "Choose another of the options, asshole")

    @patch("builtins.input", side_effect=["1", "2", "1", "1", "2", "2", "3", "3", "4", "exit"])
    def test_03_board(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as output:
            self.game.main()
        print_output = output.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['4','+','|    |    |    |    |    |    |    |']) and i]

        self.assertEqual(print_statements[0], '| 🔴 |    |    |    |    |    |    |')
        self.assertEqual(print_statements[4], '| 🔴 | 🔴 |    |    |    |    |    |')
        self.assertEqual(print_statements[8], '| 🔴 | 🔴 | 🔴 |    |    |    |    |')
        self.assertEqual(print_statements[12], '| 🔴 | 🔴 | 🔴 | 🔴 |    |    |    |')
        self.assertEqual(print_statements[13], 'Player 1 won')

    @patch("builtins.input", side_effect=["1", "2", "1", "2", "3", "4", "5", "6", "7", "exit"])
    def test_04_board(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as output:
            self.game.main()
        print_output = output.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['4','+','|    |    |    |    |    |    |    |']) and i]

        self.assertEqual(print_statements[0], '| 🔴 |    |    |    |    |    |    |')
        self.assertEqual(print_statements[1], '| 🔴 | 🔵 |    |    |    |    |    |')
        self.assertEqual(print_statements[2], '| 🔴 | 🔵 | 🔴 |    |    |    |    |')
        self.assertEqual(print_statements[3], '| 🔴 | 🔵 | 🔴 | 🔵 |    |    |    |')
        self.assertEqual(print_statements[4], '| 🔴 | 🔵 | 🔴 | 🔵 | 🔴 |    |    |')
        self.assertEqual(print_statements[5], '| 🔴 | 🔵 | 🔴 | 🔵 | 🔴 | 🔵 |    |')
        self.assertEqual(print_statements[6], '| 🔴 | 🔵 | 🔴 | 🔵 | 🔴 | 🔵 | 🔴 |')

    @patch("builtins.input", side_effect=["3", "4", "3", "4", "5", "4", "3", "4", "5", "4", "exit"])
    def test_05_board(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as output:
            self.game.main()
        print_output = output.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['4','+','|    |    |    |    |    |    |    |']) and i]

        self.assertEqual(print_statements[13], '|    |    |    | 🟡 |    |    |    |')
        self.assertEqual(print_statements[14], '|    |    |    | 🟡 |    |    |    |')
        self.assertEqual(print_statements[15], '|    |    | 🟢 | 🟡 | 🟢 |    |    |')
        self.assertEqual(print_statements[16], '|    |    | 🟢 | 🟡 | 🟢 |    |    |')
        self.assertEqual(print_statements[17], 'Player 2 won')

    @patch("builtins.input", side_effect=["1", "2", "", "0", "14", 
                                          "1", "3", "2", "4", "5", "7", "6", "1", "3", "2", "4", "5", "7", "6", 
                                          "1", "3", "2", "4", "5", "7", "6", "1", "3", "2", "4", "5", "7", "6", 
                                          "1", "3", "2", "4", "5", "7", "6", "1", "3", "2", "4", "5", "7", "6", 
                                           "exit"])
    def test_06_board_bad(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as output:
            self.game.main()
        print_output = output.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['4','+','|']) and i]

        self.assertEqual(print_statements[0], "I ask for a number between 1-8, animal")
        self.assertEqual(print_statements[1], "I ask for a number between 1-8, animal")
        self.assertEqual(print_statements[2], "I ask for a number between 1-8, animal")
        self.assertEqual(print_statements[3], "You play awfull, dude")
        self.assertEqual(print_statements[4], "Game Over")