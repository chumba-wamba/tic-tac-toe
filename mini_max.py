from helper_functions import check_winner, grid_numbering
from copy import deepcopy
from numpy import matrix


def scores(test):
    scoreDict = {
        'X': 10,
        'Tie': 0,
        '0': -10
    }

    return scoreDict[test]


def mini_max_AI(game_grid, depth, is_maxmizing):
    result = check_winner(game_grid)
    if(result[0]):
        return scores(result[1])
    if(result[0] == False and result[1] == 'Tie'):
        return scores(result[1])

    if(is_maxmizing):
        best_score = -100
        for i in range(len(game_grid)):
            for j in range(len(game_grid[i])):
                if(game_grid[i][j] == ' '):
                    game_grid[i][j] = 'X'
                    score = mini_max_AI(game_grid, depth+1, 0)
                    game_grid[i][j] = ' '
                    best_score = max(score, best_score)

        return best_score
    else:
        best_score = 100
        for i in range(len(game_grid)):
            for j in range(len(game_grid[i])):
                if(game_grid[i][j] == ' '):
                    game_grid[i][j] = '0'
                    score = mini_max_AI(game_grid, depth+1, 1)
                    game_grid[i][j] = ' '
                    best_score = min(score, best_score)

        return best_score


def best_move(game_grid):
    _, location_dict = grid_numbering(game_grid)
    best_score = -1000
    for i in range(len(game_grid)):
        for j in range(len(game_grid[i])):
            if(game_grid[i][j] == ' '):
                game_grid[i][j] = 'X'
                score = mini_max_AI(game_grid, 0, 0)
                game_grid[i][j] = ' '
                if(score > best_score):
                    best_score = score
                    move = (i, j)

    return location_dict[move]
