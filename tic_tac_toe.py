"""
Assignment: W02 Prove: Developer - Solo Code Submission
Author: Adam Dutson
"""

def main():
    player = 'x'
    grid = [1,2,3,4,5,6,7,8,9]
    display_grid(grid)
    # While loop will run while there isn't a winner.
    while check_grid(grid) == False and check_full(grid) != True:
        choice = int(input(f'{player}\'s turn to choose a square (1-9):'))
        print()
        # Checks that the user's choice isn't already taken
        if check_existing(grid, choice) == False:
            grid[choice-1] = player
            display_grid(grid)
            # Checks for a winning row before switching to new player assignment
            if check_grid(grid) == False:
                if player == 'x':
                    player = 'o'
                elif player == 'o':
                    player = 'x'
    if check_full(grid) == False:
        print(f'Good game. {player} wins. Thanks for playing!')
    else:
        print(f'This game ends in a draw. All the spaces are taken.')

def display_grid(grid):
    """Function will display the current grid variables."""
    print(f'{grid[0]}|{grid[1]}|{grid[2]}')
    print(f'-+-+-')
    print(f'{grid[3]}|{grid[4]}|{grid[5]}')
    print(f'-+-+-')
    print(f'{grid[6]}|{grid[7]}|{grid[8]}')
    print()

def check_grid(grid):
    """Function will check if current grid variables produce a winning grid result.
       If there is a winning result then the function returns TRUE. Otherwise the function
       returns FALSE."""
    win = False
    if grid[0] == grid[1] and grid[1] == grid[2]:
        win = True
    elif grid[3] == grid[4] and grid[4] == grid[5]:
        win = True
    elif grid[6] == grid[7] and grid[7] == grid[8]:
        win = True
    elif grid[0] == grid[3] and grid[3] == grid[6]:
        win = True
    elif grid[1] == grid[4] and grid[4] == grid[7]:
        win = True
    elif grid[2] == grid[5] and grid[5] == grid[8]:
        win = True
    elif grid[0] == grid[4] and grid[4] == grid[8]:
        win = True
    elif grid[2] == grid[4] and grid[4] == grid[6]:
        win = True
    else:
        win = False
    return win

def check_full(grid):
    """Function checks that there are available spaces on the grid.
       If all the spaces have been chosen then the game ends in a draw."""
    draw = True
    for i in range(9):
        if grid[i-1] != 'x' and grid[i-1] != 'o':
            draw = False
    return draw

def check_existing(grid, choice):
    """Checks to see if the users location choice is already filled.
       If there is already an 'x' or an 'o' in the chosen space this
       function will return TRUE."""
    picked = False
    if grid[choice-1] == 'x' or grid[choice-1] == 'o':
        picked = True
    return picked

if __name__ == "__main__":
    main()