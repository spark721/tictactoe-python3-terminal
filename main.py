
# import libraries if needed
import os


def render_board(board: list):
    '''
    clear the screen first \n
    render the current board
    '''
    os.system('cls||clear')
    
    print(f'\n\t {board[7]} | {board[8]} | {board[9]} ')
    print(f'\t---|---|---')
    print(f'\t {board[4]} | {board[5]} | {board[6]} ')
    print(f'\t---|---|---')
    print(f'\t {board[1]} | {board[2]} | {board[3]} \n')


def assign_player() -> dict:
    '''
    init markers as dict \n
    assign players to their marker \n
    return markers
    '''
    markers = dict()
    player1_marker = input('Player 1: Do you want to be X or O? ')
    if player1_marker == 'X':
        markers['player1'], markers['player2'] = 'X', 'O'
    elif player1_marker == 'O':
        markers['player1'], markers['player2'] = 'O', 'X'
    
    return markers


def take_user_input() -> int:
    '''
    prompt for user input and update the board \n
    return integer
    '''
    user_input = input('Please select a spot: ')
    return int(user_input)


def update_board(board: list, player_marker: str, user_input: int):
    '''
    takes in a player marker and user input \n
    update the board
    '''
    board[user_input] = player_marker


def check_game(board: list) -> bool:
    '''
    check if there is a winner

    check if the game is won, tied, lost, or ongoing \n
    return bool
    '''
    return check_winner(board):
    

def check_winner(b: list, marker: str) -> bool:
    '''
    check for 8 possible scenarios \n
    if there is a matchin scenario \n
    return True
    '''
    scenarios = {
        1: [b[1], b[2], b[3]],
        2: [b[4], b[5], b[6]], 
        3: [b[7], b[8], b[9]],
        4: [b[1], b[4], b[7]],
        5: [b[2], b[5], b[8]],
        6: [b[3], b[6], b[9]],
        7: [b[1], b[5], b[9]],
        8: [b[3], b[5], b[7]]
    }

    for win_set in scenarios.values():
        if win_set == list(marker * 3):
            return True
    return False


def game() -> bool:
    '''
    init board as a list \n
    init markers as a dict \n
    assign player markers \n
    loop until game is over \n
        render the board
        take user input
        update the board
        render the board
        check for game over, win, lose, tie
        switch the player
    prompt to play again \n
    return bool depend on play again
    '''
    board = list(' ' * 10)
    markers = assign_player()
    current_player = 'player1'
    game_over = False
    
    while not game_over:
        render_board(board)
        update_board(board, markers[current_player], take_user_input() )
        render_board(board)
        if check_winner(board, markers[current_player]):
            print(f'{current_player} has won the game!')
            break
        current_player = 'player2' if current_player == 'player1' else 'player1'
    
    play_again = input('Play again? Yes or No')
    return True if play_again == 'Yes' else False


def main():
    '''
    main function to run the game \n
    init continue flag to True \n
    loop until flag is False \n
        set flag to game()
    terminate
    '''
    flag = True
    while flag:
        flag = game()
    print('Thank you for playing')


if __name__ == "__main__":
    main()
