import random

def text_objects(text, font):
    black = (0, 0, 0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def randomCol():
    red = [(255, 0, 0), "r"]
    green = [(0, 255, 0), "g"]
    blue = [(0, 0, 255),"b"]
    white = [(255, 255, 255),"w"]
    black = [(0, 0, 0),"bl"]
    yellow = [(255,255,0),"y"]

    number = random.randint(0,6)

    if number == 1:
        return red
    elif number == 2:
        return green
    elif number == 3:
        return blue
    elif number == 4:
        return black
    elif number == 5:
        return yellow
    else:
        return white

def makeArray (A, D):
    gridCol = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    gridShape =  [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for l in range(0, D):
        for i in range(0, A):
            colour = randomCol()
            shape = randomShape()
            gridCol[i].append(colour[1])
            gridShape[i].append(shape)

    gridCol[0][0]= ""
    gridShape[0][0] = ""
    return gridCol, gridShape

def randomShape():
    circle = "c"
    square = "s"
    rectangle = "r"
    number = random.randint(0, 3)
    if number == 1:
        return circle
    elif number == 2:
        return square
    else:
        return rectangle
