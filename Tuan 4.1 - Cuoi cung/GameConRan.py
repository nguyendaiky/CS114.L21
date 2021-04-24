hash_move = {'v': [1, 0],
        '^': [-1, 0],
        '<': [0, -1],
        '>': [0, 1]}
direction = {'v': {'L': '>', 'R': '<'}, 
             '^': {'L': '<', 'R': '>'},                 
             '<': {'L': 'v', 'R': '^'}, 
             '>': {'L': '^', 'R': 'v'}}
def detecting_point(x, y, _map, snake):
    for direc in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            new = [x + direc[0], y + direc[1]]  
            try:
                if new not in snake and _map[new[0]][new[1]] == '*':
                    return new
            except:
                return None
    return None

def find_snake(_map):
    snake = []
    for x, row in enumerate(_map):
        for element in ['<', '>', 'v', '^']:
            if element in row:
                y = row.index(element)
                snake.append([x, y])
                break
    while True:
        x, y = snake[-1][0], snake[-1][1]
        new = detecting_point(x, y, _map, snake)
        if new is None:
            break
        snake.append(new)
    return snake

def snake_game(_board, _moves):
    snake = find_snake(_board)
    def next_step(snake, direc):
        x, y = pos[0] + hash_move[direc][0], pos[1] + hash_move[direc][1]
        return [x, y]
    for move in _moves:
        pos = snake[0]
        direc = _board[pos[0]][pos[1]]
        if move == 'F':
            new = next_step(snake, direc)
            if new[0] not in range(len(_board)) or new[1] not in range(len(_board[0])):
                return snake, False
            _board[new[0]][new[1]] = direc
            snake.insert(0, new)
            if new in snake[1:-1]:
                return snake, False
            snake.pop()
        else:
            _board[pos[0]][pos[1]] = direction[direc][move]
    return snake, True

def end_game(_board, moves): #avengers
    snake, alive = snake_game(_board, moves)
    direc = _board[snake[0][0]][snake[0][1]]
    new_board = []
    for i in range(len(_board)):
        new_board.append(['.'] * len(_board[0]))
    if alive:
        new_board[snake[0][0]][snake[0][1]] = _board[snake[0][0]][snake[0][1]]
        for index in snake[1:]:
            new_board[index[0]][index[1]] = '*'
    else:
        for index in snake:
            new_board[index[0]][index[1]] = 'X'
    return new_board

n, m, c = [int(x) for x in input().split()]
board = []
for index in range(n):
    board.append(list(input()))
    

moves = list(input())
new_board = end_game(board, moves)
for row in new_board:
    print(''.join(row))