import copy
while True:
    def print_game_state(game):
        for line in range(3):
            row = ''
            for column in range(3):
                row += ' ' + (game[line*3 + column] if game[line*3 + column] != '' else ' ') + ' '
                if column < 2:
                    row += '|'
            print(row)
            if line < 2:
                print('-----------')

    def check_winner(game, symbol):
        win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                         [0, 3, 6], [1, 4, 7], [2, 5, 8],
                         [0, 4, 8], [2, 4, 6]]

        for position in win_positions:
            if all(game[position_index] == symbol for position_index in position):
                return True
        return False


    def available_moves(game):
        return [index for index, field in enumerate(game) if field == '']


    def optimal_choice(game, moves, computer_player):
        if check_winner(game, 'O'):
            return 10 - moves, None
        elif check_winner(game, 'X'):
            return -10 + moves, None
        elif len(available_moves(game)) == 0:
            return 0, None

        if computer_player:
            best_score = -float('inf')
            best_move = None
            for move in available_moves(game):
                new_game = copy.deepcopy(game)
                new_game[move] = 'O'
                score, _ = optimal_choice(new_game, moves + 1, False)
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for move in available_moves(game):
                new_game = copy.deepcopy(game)
                new_game[move] = 'X'
                score, _ = optimal_choice(new_game, moves + 1, True)
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move

    game = [''] * 9

    while True:
        print_game_state(game)
        print("X turn:")
        move = int(input('Enter:\n 1 | 2 | 3\n 4 | 5 | 6\n 7 | 8 | 9\n'))
        if game[move-1] == '':
            game[move-1] = 'X'
        else:
            print("This cell is already filled. Please choose another one.")
            continue

        if check_winner(game, 'X'):
            print(f'You won!')
            break
        elif len(available_moves(game)) == 0:
            print("It's a draw!")
            break

        print_game_state(game)
        print("O turn:")

        _, computer_choice = optimal_choice(game, 0, True)
        game[computer_choice] = 'O'

        if check_winner(game, 'O'):
            print(f'Computer won!')
            break
        elif len(available_moves(game)) == 0:
            print("It's a draw!")
            break
