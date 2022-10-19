class Fullboard (Exception):
    pass

class Four_in_line():
    def __init__(self):
        self.board =[[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],]
        self.colors = {0:"  ", 1: "\U0001F534", 2: "\U0001F535", 3:"\U0001F7E2", 4:"\U0001F7E1"}
        self.player_1 = 1
        self.player_2 = 2
        self.player_turn = 1
        self.last_token = [0,0]

    def select_color(self, player, num):
        if player == 1:
            self.player_1 = num 
            self.player_turn = num
        else:
            self.player_2 = num

    def input_token(self, col):
        if col >= 7 or col < 0 or self.board[0][col] != 0:
           raise ValueError()
        for row in range(5,-1,-1):
            if self.board[row][col] == 0:
                self.board[row][col] = self.player_turn
                self.last_token =[row, col]
                break
        if self.player_turn == self.player_1:
            self.player_turn = self.player_2
        else:
            self.player_turn = self.player_1
        for colum in range(0,7):
            if self.board[0][colum] == 0:
                break
        else:
            raise Fullboard()

    def __str__(self):
        final_string = '+----'*7 + '+' + '\n'
        for row in self.board:
            for col in row:
                final_string +=  "| " + str(self.colors[col]) + " "
            final_string += '|' + '\n' + '+----'*7 + '+' + '\n'
        return final_string

    def game_end(self):
        is_winner = [None]
        is_winner.append(self.board[self.last_token[0]])
        is_winner.append(self.vertical_win())
        is_winner.append(self.SE_diagonal_win())
        is_winner.append(self.NE_diagonal_win())

        for list in is_winner:
            if list == None:
                continue
            for items in range(0, max(0,len(list)-3)):
                if list[items] == list[items+1] == list[items+2] == list[items+3] != 0:
                    return list[items]

    def vertical_win(self):
        check_list=[]
        for row in range(self.last_token[0], min(6, self.last_token[0]+4)):
            check_list.append(self.board[row][self.last_token[1]])
        return check_list

    def SE_diagonal_win(self):
        check_list=[]
        for iter in range(-3,4):
            if (iter+self.last_token[0]) < 0 or (self.last_token[1]+iter) < 0:
                continue
            try:
                check_list.append(self.board[self.last_token[0]+iter][self.last_token[1]+iter])
            except IndexError:
                continue
        if len(check_list) > 3:
            return check_list

    def NE_diagonal_win(self):
        check_list=[]
        for iter in range(-3,4):
            if (self.last_token[0]-iter) < 0 or (self.last_token[1]+iter) < 0:
                continue
            try:
                check_list.append(self.board[self.last_token[0]-iter][self.last_token[1]+iter])
            except IndexError:
                continue
        if len(check_list) > 3:
            return check_list

