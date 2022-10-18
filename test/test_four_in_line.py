import unittest
from game.four_in_line import *

class Test_four_in_line(unittest.TestCase):
    def test_00_turn(self):
        game = Four_in_line()
        self.assertEqual(game.player_turn, 1)

    def test_01_moves(self):
        game = Four_in_line()
        game.input_token(4)
        self.assertEqual(game.board[5][4], 1)
        with self.assertRaises(ValueError):
            game.input_token(9)
        self.assertEqual(game.player_turn, 2)

    def test_02_board_full(self):
        game = Four_in_line()
        for step in range(0,6):
            for elem in  [0,2,1,3,4,6,5]:
                if elem == 5 and step == 5:
                    break
                game.input_token(elem)
        with self.assertRaises(Fullboard):
            game.input_token(5)

    def test_03_vertical_win(self):
        game = Four_in_line()
        game.input_token(0)
        game.input_token(1)
        game.input_token(0)
        game.input_token(3)
        game.input_token(0)
        game.input_token(4)
        game.input_token(0)
        self.assertEqual(game.board[2], [1,0,0,0,0,0,0])
        self.assertEqual(game.board[3], [1,0,0,0,0,0,0])
        self.assertEqual(game.board[4], [1,0,0,0,0,0,0])
        self.assertEqual(game.board[5], [1,2,0,2,2,0,0])
        self.assertEqual(game.vertical_win(), [1,1,1,1])

    def test_04_NE_diagonal_win(self):
        game = Four_in_line()
        game.input_token(0)
        game.input_token(1)
        game.input_token(1)
        game.input_token(2)
        game.input_token(3)
        game.input_token(2)
        game.input_token(2)
        game.input_token(3)
        game.input_token(3)
        game.input_token(5)
        game.input_token(3)
        self.assertEqual(game.board[2], [0,0,0,1,0,0,0])
        self.assertEqual(game.board[3], [0,0,1,1,0,0,0])
        self.assertEqual(game.board[4], [0,1,2,2,0,0,0])
        self.assertEqual(game.board[5], [1,2,2,1,0,2,0])
        self.assertEqual(game.last_token, [2,3])
        self.assertEqual(game.NE_diagonal_win(), [1,1,1,1,0,0])

    def test_05_rare_wins(self):
        game = Four_in_line()
        game.board[0]=[2,2,2,2,0,0,0]
        game.last_token=[0,1]
        self.assertEqual(game.game_end(), 2)
    
    def test_06_rare_wins(self):
        game = Four_in_line()
        game.board =[[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [1,0,0,0,0,0,0],
                     [0,1,0,0,0,0,0],
                     [0,0,1,0,0,0,0],
                     [0,0,0,1,0,0,0]]
        game.last_token=[2,0]
        self.assertEqual(game.SE_diagonal_win(), [1,1,1,1])

    def test_07_rare_wins(self):
        game = Four_in_line()
        game.board =[[0,0,0,0,0,0,2],
                     [0,0,0,0,0,2,0],
                     [0,0,0,0,2,0,0],
                     [0,0,0,1,2,1,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]
        game.last_token =[0,6]
        self.assertEqual(game.NE_diagonal_win(), [1,2,2,2])

    def test_08_rare_wins(self):
        game = Four_in_line()
        game.board =[[0,0,0,1,0,0,0],
                     [0,0,0,0,1,0,0],
                     [0,0,0,0,0,1,0],
                     [0,0,0,0,0,0,1],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]
        game.last_token=[0,3]
        self.assertEqual(game.SE_diagonal_win(), [1,1,1,1])

    def test_09_rare_wins(self):
        game = Four_in_line()
        game.board =[[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,2],
                     [0,0,0,0,0,2,0],
                     [0,0,0,0,2,0,0],
                     [0,0,0,2,0,0,0]]
        game.last_token =[5,3]
        self.assertEqual(game.NE_diagonal_win(), [2,2,2,2])

    def test_10_games(self):
        game = Four_in_line()
        game.board =[[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,1,2,1,0],
                     [0,0,2,1,1,2,0],
                     [0,1,1,2,1,2,2],
                     [1,2,2,1,1,2,2]]
        game.input_token(6)
        game.input_token(3)
        self.assertEqual(game.game_end(), 2)

    def test_11_games(self):
        game = Four_in_line()
        game.board =[[0,0,0,1,2,0,0],
                     [0,0,0,0,1,1,0],
                     [0,0,0,0,0,1,1],
                     [0,0,0,0,0,0,2],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]
        game.last_token=[0,3]
        self.assertEqual(game.SE_diagonal_win(), [1,1,1,2])
        game.last_token=[0,4]
        self.assertEqual(game.SE_diagonal_win(), None)

    def test_12_games(self):
        game = Four_in_line()
        game.board =[[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,2],
                     [0,0,0,0,0,1,0],
                     [0,0,0,0,1,1,0],
                     [0,0,0,2,2,0,0]]
        game.last_token =[5,3]
        self.assertEqual(game.NE_diagonal_win(), [2,1,1,2])
        game.last_token =[5,4]
        self.assertEqual(game.NE_diagonal_win(), None)

    def test_13_games(self):
        game = Four_in_line()
        game.board =[[0,0,0,1,2,0,0],
                     [0,0,0,0,1,1,0],
                     [0,0,0,0,0,1,1],
                     [0,0,0,0,0,0,2],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]
        game.last_token=[0,3]
        self.assertEqual(game.SE_diagonal_win(), [1,1,1,2])

    def test_14_games(self):
        game = Four_in_line()
        game.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,1,2,0,0],
                      [0,0,2,1,1,2,0],
                      [0,1,1,2,1,2,2],
                      [1,2,2,1,1,2,2]]
        game.last_token = [3,2]
        self.assertEqual(game.vertical_win(),[2,1,2])
        self.assertEqual(game.SE_diagonal_win(),[0,0,2,2,1])
        self.assertEqual(game.NE_diagonal_win(),[1,1,2,1,0,0])
        self.assertEqual(game.game_end(), None)

    def test_15_infinity(self):
        for elem in range(0,70):
            self.test_00_turn()

    def test_16_games(self):
        game = Four_in_line()
        game.board = [[0,0,0,1,2,0,0],
                      [0,0,0,2,1,0,0],
                      [0,0,2,2,1,2,0],
                      [0,1,2,2,1,1,0],
                      [0,1,1,1,2,1,0],
                      [0,2,2,2,1,2,2]]
        game.last_token = [2,2]
        self.assertEqual(game.vertical_win(),[2,2,1,2])
        self.assertEqual(game.SE_diagonal_win(),[0,0,2,2,2,2])
        self.assertEqual(game.NE_diagonal_win(),[0, 1, 2, 2, 2])
        self.assertEqual(game.game_end(), 2)

    def test_17_games(self):
        game = Four_in_line()
        game.board = [[0,0,1,2,0,0,0],
                      [0,0,2,1,1,1,0],
                      [0,2,1,2,2,1,0],
                      [0,1,2,1,1,2,0],
                      [0,1,2,1,2,1,1],
                      [0,2,1,2,1,1,2]]
        game.last_token = [1,4]
        self.assertEqual(game.vertical_win(),[1,2,1,2])
        self.assertEqual(game.SE_diagonal_win(),[2,1,1,0])
        self.assertEqual(game.NE_diagonal_win(),[1,2,2,1,0])
        self.assertEqual(game.game_end(), None)

    def test_18_games(self):
        game = Four_in_line()
        game.board = [[0,0,2,1,0,0,0],
                      [0,0,1,2,0,2,1],
                      [0,2,2,2,1,2,2],
                      [0,1,1,2,1,1,2],
                      [2,1,2,1,1,1,2],
                      [1,2,1,2,1,2,1]]
        game.last_token = [2,4]
        self.assertEqual(game.vertical_win(),[1,1,1,1])
        self.assertEqual(game.SE_diagonal_win(),[2,2,1,1,2])
        self.assertEqual(game.NE_diagonal_win(),[2,2,2,1,2,0])
        self.assertEqual(game.game_end(), 1)
    
    def test_19_color(self):
        game = Four_in_line()
        game.select_color(1, 2)
        game.select_color(2, 4)
        self.assertEqual(game.player_1,2)
        self.assertEqual(game.player_2,4)

    def test_20_board(self):
        game = Four_in_line()
        board = game.format_to_ascii()
        self.assertEqual(board, "+----+----+----+----+----+----+----+\n"
                                "|    |    |    |    |    |    |    |\n"
                                "+----+----+----+----+----+----+----+\n"
                                "|    |    |    |    |    |    |    |\n"
                                "+----+----+----+----+----+----+----+\n"
                                "|    |    |    |    |    |    |    |\n"
                                "+----+----+----+----+----+----+----+\n"
                                "|    |    |    |    |    |    |    |\n"
                                "+----+----+----+----+----+----+----+\n"
                                "|    |    |    |    |    |    |    |\n"
                                "+----+----+----+----+----+----+----+\n"
                                "|    |    |    |    |    |    |    |\n"
                                "+----+----+----+----+----+----+----+\n")


# if __name__ == '__main__':
#    unittest.main()