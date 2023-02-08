

def is_empty(board, pos):
    if board[pos] == '_':
        return True
    else:
        return False


def insert_letter(board, letter, pos):
    board[pos] = letter
    return board


def print_board(board):
    count = 0

    for i in range(3):
        print('| ' + board[count] + ' | ' +
              board[count+1] + ' | ' + board[count+2] + ' |')
        count += 3


def check_win(bo, le):
    return (bo[7] == le and bo[8] == le and bo[6] == le) or (bo[4] == le and bo[5] == le and bo[3] == le) or (bo[1] == le and bo[2] == le and bo[0] == le) or (bo[0] == le and bo[4] == le and bo[8] == le) or (bo[2] == le and bo[4] == le and bo[6] == le) or (bo[0] == le and bo[3] == le and bo[6] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le)


def human_player(board, player, letter):

    check = True
    while check:
        print('Player ' + str(player) + ' turn')
        val = input('Please Select 1 - 9:')
        if val <= 9 and val >= 1:
            if is_empty(board, val-1):
                insert_letter(board, letter, val-1)
                return board
            else:
                print('Position is not empty')
        else:
            print('Input out of range')


def comp_player(board, playernum, letter):
    print('Player ' + str(playernum) + ' turn')

    player = letter
    if letter == 'O':
        opponent = 'X'
    else:
        opponent = 'O'

    possibleMoves = []
    for i in range(9):
        if board[i] == '_':
            possibleMoves.append(i)
    print(possibleMoves)
    for i in possibleMoves:
        boardCopy = board[:]
        boardCopy[i] = player
        if check_win(boardCopy, player):
            board[i] = player
            return board

    for i in possibleMoves:
        boardCopy = board[:]
        boardCopy[i] = opponent
        if check_win(boardCopy, opponent):
            board[i] = player
            return board

    if 4 in possibleMoves:
        board[4] = player
        return board

    edge = []
    for i in possibleMoves:
        if i in [0, 2, 6, 8]:
            edge.append(i)
    if len(edge) > 0:
        res = select_random(edge)
        board[res] = player
        return board

    side = []
    for i in possibleMoves:
        if i in [1, 3, 5, 7]:
            side.append(i)
    if len(side) > 0:
        res = select_random(side)
        board[res] = player
        return board

    res = select_random(possibleMoves)
    board[res] = player
    return board


def is_board_full(board):
    for i in range(9):
        if board[i] == '_':
            return False
    return True


def select_random(list):
    import random
    length = len(list)
    result = random.randint(0, length - 1)
    return list[result]


# def playTicTacToe():
#     board = ['_' for x in range(10)]
#     player1 = 'X'
#     player2 = 'O'
#     check = True
#     while check:
#         for i in range(2):
#             if i == 0:
#                 board = human_player(board, 1, player1)
#                 if check_win(board, player1):
#                     print('Player 1 Win!!!')
#                     check = False
#                     print_board(board)
#                     break

#             else:
#                 board = human_player(board, 2, player2)
#                 if check_win(board, player2):
#                     print('Player 2 Win!!!')
#                     check = False
#                     print_board(board)
#                     break
#             print_board(board)

def playTicTacToe():
    board = ['_' for x in range(10)]
    player1 = 'X'
    player2 = 'O'
    check = True
    while check:
        for i in range(2):
            if i == 0:
                board = human_player(board, 1, player1)
                if check_win(board, player1):
                    print('Player 1 Win!!!')
                    check = False
                    print_board(board)
                    break
                print(is_board_full(board))
                if is_board_full(board):
                    print('Draw game')
                    check = False
                    print_board(board)
                    break

            else:
                board = comp_player(board, 2, player2)
                if check_win(board, player2):
                    print('Player 2 Win!!!')
                    check = False
                    print_board(board)
                    break
                print(is_board_full(board))
                if is_board_full(board):
                    print('Draw game')
                    check = False
                    print_board(board)
                    break
            print_board(board)


playTicTacToe()
