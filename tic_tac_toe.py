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

if __name__ == "__main__":
    main()