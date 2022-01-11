"""
Assignment: W02 Prove: Developer - Solo Code Submission
Author: Adam Dutson
"""

def main():
    player = 'x'
    grid = [1,2,3,4,5,6,7,8,9]
    display_grid(grid)

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

if __name__ == "__main__":
    main()