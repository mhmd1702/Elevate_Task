class Board:
    def __init__(self):
        self.board = [' '] * 9
    
    def display(self):
        for i in range(3):
            print(' ' + ' | '.join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print("---|---|---")

    def update(self, position, marker):
        if self.board[position] == ' ':
            self.board[position] = marker
            return True
        return False
        
    def check_winner(self, marker):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.board[i] == marker for i in condition) for condition in win_conditions)
    
    def is_full(self):
        return ' ' not in self.board
    
    def reset(self):
        self.board = [' '] * 9

class Game:
    def __init__(self):
        self.board = Board()
        self.current_marker = 'X'
        self.players = {'X': 'Player 1', 'O': 'Player 2'}

    def switch_player(self):
        self.current_marker = 'O' if self.current_marker == 'X' else 'X'

    def get_move(self):
        while True:
            try:
                position = int(input(f'{self.players[self.current_marker]}, enter your move (1-9): ')) - 1
                if position in range(9) and self.board.update(position, self.current_marker):
                    break
                print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

    def play(self):
        while True:
            self.board.display()
            self.get_move()
            if self.board.check_winner(self.current_marker):
                self.board.display()
                print(f"{self.players[self.current_marker]} wins!")
                break
            if self.board.is_full():
                self.board.display()
                print("It's a tie!")
                break
            self.switch_player()

    def start(self):
        while True:
            self.play()
            if input("Play again? (y/n): ").lower() != 'y':
                break
            self.board.reset()
            self.current_marker = 'X'

if __name__ == '__main__':
    game = Game()
    game.start()
