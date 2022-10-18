from .four_in_line import Fullboard, Four_in_line

game = Four_in_line()
class Interfaz ():

    def main (self, num=1):
        if num == 0:
            return True
        feedback = input("""You want to play the fantastic game of *Four in Line*!!??
        Send *play* to 811-0800-2615 RIGHT NOW
        """)
        if feedback != "play":
            print("FUCK 0FF")
        else:
            player = 1
            while player < 3:
                print([f'{key} {value}' for key,value in game.colors.items() if key != 0 and key != game.player_1])
                color = input("  Choose color for player " + str(player) + " : ")
                try:
                    int(color)
                except ValueError:
                    print("""
            Write a number, asshole
                    """)
                    continue
                if not (int(color) in game.colors.keys()) or int(color) == 0:
                    print("""
            Choose one of the options, asshole
                    """)
                    continue
                else:
                    game.select_color(player, int(color))
                    player += 1
            player = 1

            while game.game_end() == None:
                print(game.format_to_ascii())
                feedback = input("Player " + str(player) + ": Pick a column ")
                if feedback == "":
                    print("I ask for a number between 1-8, animal")
                    continue
                if feedback == "exit":
                    break
                try:
                    game.input_token(int(feedback)-1)
                except ValueError or Fullboard():
                    print("I ask for a number between 1-8, animal")
                    continue
                if player == 1:
                    player = 2
                else:
                    player = 1
            else:
                print(game.format_to_ascii())
                if (game.game_end() % game.player_1) == 0:
                    print("Player 1 won")
                else:
                    print("Player 2 won")
            print("Game Over")

