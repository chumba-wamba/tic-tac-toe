def grid(side=3):
    game_grid = [[' ' for i in range(side)] for j in range(side)]

    return game_grid


def grid_numbering(game_grid):
    number_dict = {

    }

    location_dict = {

    }

    counter = 0
    for i in range(len(game_grid)):
        for j in range(len(game_grid[i])):
            counter += 1
            number_dict[counter] = (i, j)
            location_dict[(i, j)] = counter

    return number_dict, location_dict


def check_winner(game_grid):
    victory, winner = False, None

    columns = []
    for i in range(len(game_grid)):
        columns.append([game_grid[j][i] for j in range(len(game_grid))])

    diagonal_one, diagonal_two = [], []
    for i in range(len(game_grid)):
        for j in range(len(game_grid)):
            if(i == j):
                diagonal_one.append(game_grid[i][j])
            if(i+j == len(game_grid)-1):
                diagonal_two.append(game_grid[i][j])

    for row in game_grid:
        if(all((x == row[0] and x != ' ') for x in row)):
            victory = True
            if(row[0] == 'X'):
                winner = 'X'
            elif(row[0] == '0'):
                winner = '0'

    for column in columns:
        if(all((x == column[0] and x != ' ') for x in column)):
            victory = True
            if(column[0] == 'X'):
                winner = 'X'
            elif(column[0] == '0'):
                winner = '0'

    if(all((x == diagonal_one[0] and x != ' ') for x in diagonal_one)):
        victory = True
        if(diagonal_one[0] == 'X'):
            winner = 'X'
        elif(diagonal_one[0] == '0'):
            winner = '0'
    if(all((x == diagonal_two[0] and x != ' ') for x in diagonal_two)):
        victory = True
        if(diagonal_two[0] == 'X'):
            winner = 'X'
        elif(diagonal_two[0] == '0'):
            winner = '0'

    counter = 0
    for i in range(len(game_grid)):
        for j in range(len(game_grid[i])):
            if(game_grid[i][j] == ' '):
                counter += 1

    if(counter == 0 and winner == None):
        winner = 'Tie'

    return [victory, winner]
