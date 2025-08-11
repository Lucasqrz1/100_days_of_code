class TicTacToe:
    def __init__(self):
        # Think of the board like a 3x3 grid of empty spaces
        self.board = [' ' for _ in range(9)]  # 9 positions numbered 1-9
        self.current_player = 'X'  # X always goes first
    
    def display_board(self):
        """Show the current board state"""
        print("\n Current Board:")
        print("   |   |   ")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("   |   |   ")
        
        # Show position numbers for reference
        print("\n Position numbers:")
        print("   |   |   ")
        print(" 1 | 2 | 3 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 4 | 5 | 6 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 7 | 8 | 9 ")
        print("   |   |   ")

    
    def is_valid_move(self, position):
        """Check if the move is allowed"""
        # Position must be 1-9 and that spot must be empty
        return 1 <= position <= 9 and self.board[position - 1] == ' '
    
    def make_move(self, position):
        """Place the current player's symbol on the board"""
        if self.is_valid_move(position):
            self.board[position - 1] = self.current_player
            return True
        return False
    
    def check_winner(self):
        """Check if someone won the game"""
        # All possible winning combinations (like connecting the dots)
        winning_combinations = [
            # Rows
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            # Columns  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            # Diagonals
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != ' '):
                return self.board[combo[0]]  # Return the winner (X or O)
        
        return None  # No winner yet
    
    def is_board_full(self):
        """Check if all spaces are taken"""
        return ' ' not in self.board
    
    def switch_player(self):
        """Switch between X and O"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def play_game(self):
        """Main game loop - like the game's heartbeat"""
        print("Welcome to Tic Tac Toe!")
        print("Players take turns placing X and O")
        print("First to get 3 in a row wins!")
        
        while True:
            self.display_board()
            
            # Get player's move
            try:
                print(f"\nPlayer {self.current_player}'s turn")
                position = int(input("Choose position (1-9): "))
            except ValueError:
                print("Please enter a number between 1 and 9!")
                continue
            
            # Try to make the move
            if not self.make_move(position):
                print("Invalid move! Try again.")
                continue
            
            # Check if someone won
            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"\n🎉 Player {winner} wins! 🎉")
                break
            
            # Check if it's a tie
            if self.is_board_full():
                self.display_board()
                print("\n🤝 It's a tie! Good game!")
                break
            
            # Switch to the other player
            self.switch_player()
    
    def play_again(self):
        """Ask if players want another round"""
        while True:
            choice = input("\nPlay again? (y/n): ").lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no")

def main():
    """Start the game"""
    print("=" * 40)
    print("  TIC TAC TOE - TEXT VERSION")
    print("=" * 40)
    
    while True:
        game = TicTacToe()
        game.play_game()
        
        if not game.play_again():
            print("Thanks for playing! Goodbye! 👋")
            break

# Run the game
if __name__ == "__main__":
    main()