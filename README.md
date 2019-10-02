# Tic Tac Toe

## Overview
This is a text-based tic tac toe game for terminal or command prompt

My very first project in Python!

## Tools used
- python 3.7.4

## Instruction
- This project must be run with Python 3.6 or above

- Check your python version

        $ python --version

        $ python3 --version

- Execute main.py with python3
        
        $ python3 main.py

- Game board
    - The slots are numbered as below. Just as in a computer keyboard's number pad.

    ```
         7 | 8 | 9 
        ---|---|---
         4 | 5 | 6 
        ---|---|---
         1 | 2 | 3 
    ```

## Feature
- Input validation / exception handling
    - Implemented exception handling feature for all user inputs with `try`, `except`, `else` block
    
        For example,

        ```python
        def take_user_input() -> int:
            '''
            prompt for user input \n
            return integer
            '''
            while True:
                user_input = input('Please select a spot: ')
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
        ```

- type hints
    - `function annotations` for arguments and return value

        For example, below function takes in board as a `list` and a marker as a `str` then returns a `bool` value

        ```python
        def check_winner(b: list, marker: str) -> bool:
        ``` 

    - `variable annotations`

        Examples,
        ```python
        user_input: int = take_user_input(current_player, player_marker)
        ```

        ```python
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
        ```
