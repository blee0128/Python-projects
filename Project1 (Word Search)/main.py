# CSCI 1913 Fall 2022
# Author: (Your name here)

# QUESTIONS -- DO THESE LAST.
# Assumptions: assume the letter grid has width W and height H
# Further assume the word parameter has length L (for find) and than the max_len parameter is L (for extract)
# Finally, Assume that concatenating a letter to a string takes time O(1)
# List any other assumptions you make.

# For each question below, answer your questions by filling in the provided multi-line strings.
# (yes it's a bit of a hokey way to do this, but it should work well enough and it keeps the answers in 1 file)
# For each question state any extra assumptions you made, and explain your answer.
# An incorrect answer with no explanation will get no partial credit.

# Question 1: What is the worst-case big-O runtime of your get_size function?
import random
Question1 = '''
answer
'''

# Question 2: What is the worst-case big-O runtime of your copy_word_grid function?
Question2 = '''
answer
'''

# Question 3: What is the worst-case big-O runtime of your extract function?
Question3 = '''
answer
'''

# Question 4: What is the worst-case big-O runtime of your find function?
Question4 = '''
answer
'''

# LEAVE THESE LINES ALONE BEGIN:
# So the code I provide at the bottom needs these lines of code.

# This code defines valid directions a word can travel.
# Each direction is a tuple (dx, dy) that says how you change x and y
# coordinates to go in a given direction.
RIGHT = (1, 0)       # to go right add 1 to x
DOWN = (0, 1)         # to go down add 1 to y
RIGHT_DOWN = (1, 1)  # to go right_down add 1 to both x and y
RIGHT_UP = (1, -1)    # to go right_up add 1 to x and subtract 1 from y
DIRECTIONS = (RIGHT, DOWN, RIGHT_DOWN, RIGHT_UP)
# Good use of these direction-tuples makes for much easier programs for this project. assignment.

# LEAVE THESE LINES ALONE END:


def get_size(word_grid):
    x = len(word_grid[0])
    y = len(word_grid)
    return (x, y)


def print_word_grid(word_grid):
    string = ""
    for i in word_grid:
        for j in i:
            string += j
        string += '\n'
    print(string)


def copy_word_grid(word_grid):
    y = [row[:] for row in word_grid]
    return y


def extract(word_grid, position, direction, max_len):
    max_x, max_y = get_size(word_grid)
    pos_x, pos_y = position
    dir_x, dir_y = direction
    string = ""

    for i in range(max_len):
        if pos_x < max_x and pos_y < max_y and pos_x >= 0 and pos_y >= 0:
            string += word_grid[pos_y][pos_x]
            pos_x += dir_x
            pos_y += dir_y
        else:
            return string

    return string


def find(word_grid, word):
    for i in range(len(word_grid)):
        for j in range(len(word_grid[i])):
            for k in DIRECTIONS:
                x = extract(word_grid, (j, i), k, len(word))
                if x == word:
                    return ((j, i), k)

    return None


def show_solution(word_grid, word):
    x = find(word_grid, word)
    if x == None:
        print(word + " is not found in this word search")
    else:
        pos, dir = x
        pos_x, pos_y = pos
        dir_x, dir_y = dir
        wordfound = word.capitalize()
        print(wordfound + " can be found as below")

        wgcopy = copy_word_grid(word_grid)
        for i in range(len(word)):
            x = word_grid[pos_y][pos_x]
            x1 = x.capitalize()
            wgcopy[pos_y][pos_x] = x1
            pos_x, pos_y = pos_x + dir_x, pos_y + dir_y

        print_word_grid(wgcopy)


def make_empty_grid(width, height):
    return [['?' for x in range(width)] for y in range(height)]


def can_add_word(word_grid, word, position, direction):
    pos_x, pos_y = position
    dir_x, dir_y = direction
    x = extract(word_grid, position, direction, len(word))
    if len(x) == len(word):
        for i in word:
            if word_grid[pos_y][pos_x] == '?':
                pos_x, pos_y = pos_x + dir_x, pos_y + dir_y
            elif word_grid[pos_y][pos_x] == i:
                pos_x, pos_y = pos_x + dir_x, pos_y + dir_y
            else:
                return False
        return True
    else:
        return False


def do_add_word(word_grid, word, position, direction):
    pos_x, pos_y = position
    dir_x, dir_y = direction

    for i in word:
        word_grid[pos_y][pos_x] = i
        pos_x += dir_x
        pos_y += dir_y

    return word_grid


def fill_blanks(word_grid):
    import random
    import string

    for i in range(len(word_grid)):
        for j in range(len(word_grid[i])):
            if word_grid[i][j] == '?':
                word_grid[i][j] = random.choice(string.ascii_letters).lower()

    return word_grid

####
#
#  PROVIDED CODE -- You shouldn't need to change any of this.
#  (it's not that we didn't think you could write this, it's this stuff is either
#  1) really easy and not worth putting in a 1913 project or
#  2) really, really specific. (it's hard to describe the correct function of
#     these two functions without just telling you exactly how to do it.)
#
#  These are provided to "complete" the project -- I.E. these work with the code you write and allow you to use your
#  functions to generate word-searches for personal use. It is RECOMMENDED that you build a front-end for this behavior
#  so you can more easily use and play-with the finished product.
####


def add_word(word_grid, word):
    ''' Attempts to '''
    width, height = get_size(word_grid)
    for attempt_num in range(50):
        direction = random.choice(DIRECTIONS)
        x = random.randrange(width)
        y = random.randrange(height)
        location = (x, y)
        if can_add_word(word_grid, word, location, direction):
            do_add_word(word_grid, word, location, direction)
            return True
    return False


def generate(width, height, words):
    words_actual = []
    word_grid = make_empty_grid(width, height)
    for word in words:
        if add_word(word_grid, word):
            words_actual.append(word)
    fill_blanks(word_grid)
    return word_grid, words_actual


wg = [['p', 'c', 'n', 'd', 't', 'h', 'g'],
      ['w', 'a', 'x', 'o', 'a', 'x', 'f'],
      ['o', 't', 'w', 'g', 'd', 'r', 'k'],
      ['l', 'j', 'p', 'i', 'b', 'e', 't'],
      ['f', 'v', 'l', 't', 'o', 'w', 'n']]


# wgcopy = copy_word_grid(wg)
# wg[0][0] = 'a'
# x = print_word_grid(wg)
# print("ori")
# print(x)
# y = print_word_grid(wgcopy)
# print("copy")
# print(y)
# x = extract(wg, (5, 2), DOWN, 5)
# print(x)
# x = show_solution(wg, "cat")
# x = make_empty_grid(3, 2)
# x[0][0] = 'q'
# x[0][1] = 'k'
# print(x)
# y = fill_blanks(x)
# print(y)
# x = find(wg, "cxgok")
# print(x)
grid, words = generate(
    10, 10, ["java", "python", "list", "set", "tuple", "string"])
# print_word_grid(grid)
