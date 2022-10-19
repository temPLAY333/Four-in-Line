from .four_in_line import Fullboard, Four_in_line


class Interfaz ():
    def __init__(self):
        self.game = Four_in_line()

    def choose_color(self):
        player = 1
        while player < 3:
            print([f'{key} {value}' for key,value in self.game.colors.items() if key != 0])
            color = input("  Choose color for player " + str(player) + " : ")
            try:
                int(color)
            except ValueError:
                print("Write a number, asshole")
                continue
            if not (int(color) in self.game.colors.keys()) or int(color) == 0:
                print("Choose one of the options, asshole")
                continue
            elif (int(color) == self.game.player_1) and player == 2:
                print("Choose another of the options, asshole")
                continue
            else:
                self.game.select_color(player, int(color))
                player += 1

    def main (self):
        self.choose_color()    
        player = 1
        while self.game.game_end() == None:
            print(self.game.__str__())
            feedback = input("Player " + str(player) + ": Pick a column ")
            if feedback == "":
                print("I ask for a number between 1-8, animal")
                continue
            if feedback == "exit":
                break
            try:
                self.game.input_token(int(feedback)-1)
            except ValueError:
                print("I ask for a number between 1-8, animal")
                continue
            except Fullboard:
                print("You play awfull, dude")
                break
            if player == 1:
                player = 2
            else:
                player = 1
        else:
            print(self.game.__str__())
            if (self.game.game_end()) == self.game.player_1:
                print("Player 1 won")
            else:
                print("Player 2 won")
        print("Game Over")

