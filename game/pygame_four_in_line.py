import pygame
from game.four_in_line import *

class Game_four_in_line():
    def __init__(self):
        self.game = Four_in_line()
        self.screen = pygame.display.set_mode((1050,1050))
        self.colors = {0:(0,0,0), 1:(255,0,0), 2:(0,0,255), 3:(255,255,0), 4: (0,255,0)}
        self.token_1 = 1
        self.token_2 = 2
        self.my_font = pygame.font.SysFont('Comic Sans MS', 120)
        
    def board(self):
        self.screen.fill((100,100,100))
        posi = 75
        for row in range(0,6):
            for col in range(0,7):
                pygame.draw.circle(self.screen, self.colors[self.game.board[row][col]],
                                   (posi+150*col,3*posi+150*row), 50)
    
    def token_fall(self, col):
        value = 0
        for num in range(0,6):
            if self.game.board[num][col] != 0:
                value = num+1
                break
        else:
            value = 7

        if value == 1:
            raise Fullboard()

        for y in range(0,value*15):
            self.board()
            pygame.draw.circle(self.screen, self.colors[self.game.player_turn],
                                   (col*150+75, 10*y - 65), 50)
            pygame.display.flip()
        pygame.event.clear()

    def choose_color(self, player):
        posi_color = 150
        selector = 1

        while True:
            self.screen.fill((100,100,100))
            text = self.my_font.render(f"Player {player} choose color: ", False, (0, 0, 0))
            self.screen.blit(text, (100,50))

            pygame.draw.circle(self.screen, (0,0,0),
                                (posi_color+selector*150, posi_color+50), 60) 

            for color in range(1,5):
                pygame.draw.circle(self.screen, self.colors[color],
                                (posi_color+color*150, posi_color+50), 50) 

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pass
                    elif event.key == pygame.K_RIGHT and selector != 4:
                        selector += 1
                    elif event.key == pygame.K_LEFT and selector != 1:
                        selector -= 1  
                    elif event.key == pygame.K_DOWN:
                        if selector == self.game.player_1 and player != 1:
                            text = self.my_font.render("Choose other color", False, (0, 0, 0))
                            self.screen.blit(text, (120,300))

                            text = self.my_font.render("ASSHOLE", False, (0, 0, 0))
                            self.screen.blit(text, (260,400))

                            pygame.display.flip()
                            pygame.time.delay(1300)
                            pygame.event.clear()
                            break
                        self.game.select_color(player, selector)
                        return None
                        
            pygame.display.flip()

    def main(self):    
        posi_token = 75
        self.choose_color(1)
        self.choose_color(2)
        while self.game.game_end() == None:
            self.board()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pass
                    elif event.key == pygame.K_RIGHT and posi_token != 975:
                        posi_token += 150
                    elif event.key == pygame.K_LEFT and posi_token != 75:
                        posi_token -= 150
                    elif event.key == pygame.K_DOWN:
                        try:
                            self.token_fall((posi_token-75)//150)
                            self.game.input_token((posi_token-75)//150)
                        except Fullboard:
                            text = self.my_font.render("It's full there, idiot", False, (0, 0, 0))
                            self.screen.blit(text, (150,50))
                            pygame.display.flip()
                            pygame.time.delay(1300)
                            pygame.event.clear()

            pygame.draw.circle(self.screen, self.colors[self.game.player_turn],
                                   (posi_token, 75), 50) 
            pygame.display.flip()

        self.board()
        pygame.font.init()
        if self.game.game_end() == self.game.player_1:
            posi_token = 1
        else:
            posi_token = 2
        text = self.my_font.render(f'The Winner is Player {posi_token}', False, (0, 0, 0))
        self.screen.blit(text, (70,50))
        pygame.display.flip()

        pygame.time.delay(1500)
        pygame.quit()



if __name__ == "__main__":
    pygame.init()
    games = Game_four_in_line()
    games.main()

            




