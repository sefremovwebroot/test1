# https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
# Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

###
# https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
# Remove String Spaces
def no_space(x):
    return "".join(x.split())

###
# https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
# Remove String Spaces
no_space = lambda s: ''.join(filter(lambda ch: not ch == ' ', s))

###
# https://www.codewars.com/kata/grasshopper-terminal-game-move-function/train/python
# Grasshopper - Terminal game move function
def move(position, roll):
    return position + roll * 2

###
# https://www.codewars.com/kata/grasshopper-terminal-game-move-function/train/python
# Grasshopper - Terminal game move function
move = lambda p, r : p + r * 2