import random


# creating the mat
def start_Game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat


# adding 2 in random positions
def add_new_two(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2


# checking the current status of game
def current_state_game(mat):
    # Anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'Won'
    # if 0 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'Game not Over'
    # for every row and column except the last row and column
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                return 'GAME not Over'
    # for last row
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'Game not Over'
    # for last column
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'Game not Over'
    # when all the above condition fails
    return 'Lost'


def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed


def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j]*2
                mat[i][j+1] = 0
                changed = True
    return mat, changed


def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat


def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat


def move_up(grid):
    transpose_mat = transpose(grid)
    compress_mat, change1 = compress(transpose_mat)
    merge_mat, change2 = merge(compress_mat)
    changed = change1 or change2
    compress_mat, temp = compress(merge_mat)
    transpose_mat = transpose(compress_mat)
    return transpose_mat, changed


def move_down(grid):
    transpose_mat = transpose(grid)
    reverse_mat = reverse(transpose_mat)
    compress_mat, change1 = compress(reverse_mat)
    merge_mat, change2 = merge(compress_mat)
    changed = change1 or change2
    compress_mat, temp = compress(merge_mat)
    reverse_mat = reverse(compress_mat)
    transpose_mat = transpose(reverse_mat)
    return transpose_mat, changed


def move_right(grid):
    reverse_mat = reverse(grid)
    compress_mat, change1 = compress(reverse_mat)
    merge_mat, change2 = merge(compress_mat)
    changed = change1 or change2
    compress_mat, temp = compress(merge_mat)
    reverse_mat = reverse(compress_mat)
    return reverse_mat, changed


def move_left(grid):
    compress_mat, change1 = compress(grid)
    merge_mat, change2 = merge(compress_mat)
    changed = change1 or change2
    compress_mat, temp = compress(merge_mat)
    return compress_mat, changed


