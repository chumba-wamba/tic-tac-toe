from mini_max import scores, mini_max_AI, best_move
from helper_functions import grid, grid_numbering, check_winner
import random
import time
import copy
from numpy import matrix


def grid_update(temp_grid, location, x_or_zero, number_dict, user):
    while(temp_grid[number_dict[location][0]][number_dict[location][1]] != ' '):
        if(user == 1):
            location = int(input("Re-enter the location: "))
        else:
            location = best_move(temp_grid)
    x, y = number_dict[location]
    temp_grid[x][y] = x_or_zero

    return temp_grid


def tic_tac_toe(game_grid):
    temp_grid = copy.deepcopy(game_grid)
    number_display_grid = copy.deepcopy(game_grid)
    number_dict, location_dict = grid_numbering(game_grid)

    for i in range(len(number_display_grid)):
        for j in range(len(number_display_grid)):
            if(len(str(location_dict[(i, j)])) == 1):
                number_display_grid[i][j] = str(location_dict[(i, j)])+' '
            else:
                number_display_grid[i][j] = str(location_dict[(i, j)])

    print('Grid locations and their numbering:')
    print(matrix(number_display_grid))

    time.sleep(1)
    for i in range(len(temp_grid)*len(temp_grid)):
        # computer_location=best_move(temp_grid)
        computer_location = 1
        temp_grid = grid_update(
            temp_grid, computer_location, 'X', number_dict, 0)

        print('Computer:')
        print(matrix(temp_grid))
        if(check_winner(temp_grid)[0]):
            print(f'{check_winner(temp_grid)[1]} Won')
            break
        if(check_winner(temp_grid)[0] == False and check_winner(temp_grid)[1] == 'Tie'):
            print(f'Tie')
            break

        player_location = int(input("Enter the location: "))
        temp_grid = grid_update(temp_grid, player_location, '0', number_dict, 1)

        print('Player:')
        print(matrix(temp_grid))
        if(check_winner(temp_grid)[0]):
            print(f'{check_winner(temp_grid)[1]} Won')
            break
        if(check_winner(temp_grid)[0] == False and check_winner(temp_grid)[1] == 'Tie'):
            print(f'Tie')
            break

        time.sleep(1)
