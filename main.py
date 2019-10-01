
# import libraries if needed
import os
from typing import Dict, List


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
    os.system('cls||clear')

    markers: Dict[str, str] = dict()
    while True:
        player1_marker = input('\n\nPlayer 1: Do you want to be X or O? ')
        if player1_marker.lower() == 'x':
            markers['player1'], markers['player2'] = 'X', 'O'
            break
        elif player1_marker.lower() == 'o':
            markers['player1'], markers['player2'] = 'O', 'X'
            break
    
    return markers


def take_user_input(current_player: str, player_marker: str) -> int:
    '''
    prompt for user input \n
    return integer
    '''
    while True:
        user_input = input(f'{current_player}, you are \'{player_marker}\'\nplease select a spot: ')
        try:
            int(user_input)
        except:
            print(f'\tinvalid input: {user_input}\n')
            continue
        else:
            if int(user_input) >= 1 and int(user_input) <= 9:
                return int(user_input)
            else:
                print(f'\tinvalid input: {user_input}\n')


def update_board(board: list, player_marker: str, current_player: str) -> list:
    '''
    takes in board and player marker \n
    grab player input \n
    update and return the board
    '''
    user_input = take_user_input(current_player, player_marker)

    while board[user_input] != ' ':
        print(f'\tslot {user_input} has been already taken\n')
        user_input = take_user_input(current_player, player_marker)

    board[user_input] = player_marker
    return board


def check_winner(b: list, marker: str) -> bool:
    '''
    check for 8 possible scenarios \n
    if there is a matchin scenario \n
    return True
    '''
    scenarios: Dict[int, list] = {
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


def check_tie(b: list) -> bool:
    '''
    check the board to see if there is a tie \n
    return bool
    '''
    for i in range(1, len(b)):
        if b[i] == ' ': return False
    return True


def play_again() -> bool:
    while True:
        play_again = input('\nPlay again? (Yes or No) ')
        if play_again.lower() == 'yes':
            return True
        elif play_again.lower() == 'no':
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
        board = update_board(board, markers[current_player], current_player)
        render_board(board)
        if check_winner(board, markers[current_player]):
            print(f'{current_player} has won the game!')
            break
        elif check_tie(board):
            print('Game Over')
            break
        current_player = 'player2' if current_player == 'player1' else 'player1'
    
    return play_again()


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
    print('\nThank you for playing\n')


if __name__ == "__main__":
    main()
