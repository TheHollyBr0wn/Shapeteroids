import pygame
import time
from gameFuncs import *
debug = False 

#### For the first 5 seconds, a baddie would appear, then disapear. if you land on bad dude you loose
#### SOUND
#### HIGH SCORE
#### COMMENT CODE

pygame.init()
timer = int(time.time())
screen = pygame.display.set_mode((700, 500))

# Title and Icon
pygame.display.set_caption("Shapeteroids v0.9")
icon = pygame.image.load('move.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('war.png')
playerX = 60
playerY = 25
playerX_change = 0
playerY_change = 0

def message_display(text,x,y,size):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((x),(y))
    screen.blit(TextSurf, TextRect)

def player(x,y):
    # Blit draws image onto page
    screen.blit(playerImg, (x,y))

def keyShape(colour,shape):
    x = 570
    y = 90
    if colour[1] == "r":
        colour = (255, 0, 0)
    elif colour[1] == "g":
        colour = (0, 255, 0)
    elif colour[1] == "b":
        colour = (0, 0, 255)
    elif colour[1] == "w":
        colour = (255, 255, 255)
    elif colour[1] == "y":
        colour = (255, 255, 0)
    else:
        colour = (0, 0, 0)

    if shape == 's':
        pygame.draw.rect(screen, colour, (x, y, 30, 30))
    elif shape == 'c':
        pygame.draw.circle(screen, colour, (x + 20, y + 15), 20)
    elif shape == 'r':
        pygame.draw.polygon(screen, colour, ((x + 15, y - 5), (x - 5, y + 32), (x + 35, y + 32)))

def drawInfo(xOff, yOff,lives,score):
    pygame.draw.line(screen, black, (xOff + 500, yOff + 125), (xOff + 500, yOff + 575), 5)
    pygame.draw.line(screen, black, (xOff + 675, yOff + 125), (xOff + 675, yOff + 575), 5)
    pygame.draw.line(screen, black, (xOff + 675, yOff + 375), (xOff + 500, yOff + 375), 5)
    pygame.draw.line(screen, black, (xOff + 675, yOff + 125), (xOff + 500, yOff + 125), 5)
    pygame.draw.line(screen, black, (xOff + 675, yOff + 250), (xOff + 500, yOff + 250), 5)
    pygame.draw.line(screen, black, (xOff + 675, yOff + 475), (xOff + 500, yOff + 475), 5)
    pygame.draw.line(screen, black, (xOff + 675, yOff + 575), (xOff + 500, yOff + 575), 5)
    message_display('Key shape', xOff + 590, yOff + 160, 20)
    message_display('Number of lives', xOff + 588, yOff + 290, 20)
    message_display('Score', xOff + 590, yOff + 400, 20)
    message_display('Bonus', xOff + 590, yOff + 500, 20)
    message_display(score,xOff + 590, yOff + 440,30)
    message_display(lives, xOff + 590, yOff + 330, 30)

def drawGrid(colourGrid, shapeGrid):
    x = 25
    y = 25
    across=0
    down=0
    for eachRow in colourGrid:
        for eachItem in eachRow:
            if eachItem == "r":
                colour = (255, 0, 0)
            elif eachItem == "g":
                colour = (0, 255, 0)
            elif eachItem == "b":
                colour = (0, 0, 255)
            elif eachItem == "w":
                colour  = (255, 255, 255)
            elif eachItem == "y":
                colour = (255,255,0)
            else:
               colour = (0, 0, 0)

            if shapeGrid[down][across] == 's':
                pygame.draw.rect(screen, colour, (x, y, 32, 32))
            elif shapeGrid[down][across] == 'c':
                pygame.draw.circle(screen, colour, (x+16, y+16), 20)
            elif shapeGrid[down][across] == 'r':
                pygame.draw.polygon(screen, colour, ((x+15, y-5), (x-5, y+31), (x+35, y+31)))
            x = x + 80
            across = across + 1
        across = 0
        down = down + 1

        x = 25
        y = y + 70

def legalMove(gCol,gShape,col,shape,pX,pY,cnt):
    # function to determine whether or not a players move is legal
    # gCol = a list of lists containing all the colours on the whole grid
    # gShape = a list of lists containing all the shapes on the whole grid
    # col = the current okay colour, e.g.'g'
    # shape = the current okay shape
    # pX, pY = player postion (0-6)
    # returns True for legal move

    if gCol[pY][pX] == col or gShape[pY][pX] == shape:
        cnt = cnt + 1
        return 0, cnt
    elif gCol[pY][pX] == "":
        return 1, cnt
    else:
        global debug

        if debug:
            cnt = cnt + 1
            return 0, cnt
        else:
            cnt = cnt + 1
            return 2, cnt

# game loop
running = True
gameState = 0
X = 25
Y = 25
playerX = 0
playerY = 0
Score = 0
speed = 3
Lives = 3
doneyet = False
counter = 0
valid = 0
bonus = 4000
colour = randomCol()
shape = randomShape()

while running == True:
    if gameState == 0:      ###  GAME STATE 1 ####
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            screen.fill((128, 128, 128))
            grey = (128, 128, 128)
            pygame.draw.rect(screen, grey, (0, 0, 700, 500))
            message_display('Instructions',350, 100, 30)
            message_display('Aim to get rid of all the shapes', 350, 150, 20)
            message_display('Must be the same colour or shape as the Key Shape', 350, 200, 20)
            message_display('Remember where the monster is! ', 350, 250, 20)
            message_display('Finish before the bonus and you will get extra points', 350, 300, 20)
            message_display('Click anywhere to continue', 350, 400, 15)
            pygame.display.update()
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] == True:
                tim = int(time.time())
                gameState = gameState + 1

    if gameState == 1:              ### GAME STATE 2 ###
        screen.fill((128, 128, 128))
        across = 7
        down = 6
        thing1, thing2 = makeArray(across,down)
        drawGrid(thing1,thing2)
        gameState = gameState + 1
        gridCol = thing1
        gridShape = thing2

    if gameState == 2:              ### GAME STATE 3 ###
        newMove = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if keystroke is pressed check if right/left
            if event.type == pygame.KEYDOWN: # key down is when key is pressed
                if event.key == pygame.K_LEFT:
                    playerX = playerX - 1
                    if playerX < 0:
                        playerX = 0
                    newMove = True
                elif event.key == pygame.K_RIGHT:
                    playerX = playerX + 1
                    if playerX > 5:
                        playerX = 5
                    newMove = True
                elif event.key == pygame.K_UP:
                    playerY = playerY - 1
                    if playerY < 0:
                        playerY = 0
                    newMove = True
                elif event.key == pygame.K_DOWN:
                    playerY = playerY + 1
                    if playerY > 6:
                        playerY = 6
                    newMove = True
                else:
                    newMove = False

                X = 25+(playerX*80)
                Y = 25+(playerY*70)
                # Decides if legal move or not
                colour1 = colour[1]
                valid,counter = legalMove(gridCol, gridShape, colour1, shape, playerX, playerY,counter)

                if valid == 0:
                    Score = Score + 10
                elif valid == 2:
                    Lives = Lives - 1

                gridCol[playerY][playerX] = ""
                gridShape[playerY][playerX] = ""
             
                if Lives == 0 or counter == 41:
                    gameState = 3
            if newMove:
                player(X, Y)
                pygame.display.update()
        grey = (128, 128, 128)
        pygame.draw.rect(screen, grey, (0, 0, 800, 600))

        ## lives and draws info
        xOff = 0
        yOff = -100
        black = (0, 0, 0)
        score = str(Score)
        lives = str(Lives)
        drawInfo(xOff, yOff,lives,score)

        ## Shape selector

        seconds = int(time.time())
        if timer == seconds - speed:
            colour = randomCol()
            shape = randomShape()
            timer = seconds
        keyShape(colour,shape)

        ## Bonus
        num = int(time.time())
        TOT = num - tim
        bonus = 400 - (6*TOT)
        bonus = str(bonus)
        message_display(bonus, 590, 440, 30)

        ## redraws grid and player
        drawGrid(thing1,thing2)
        player(X, Y)
        pygame.display.update()
    if gameState == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grey = (128, 128, 128)
        pygame.draw.rect(screen, grey, (0, 0, 700, 500))

        if Score >= 399:
            message_display('YOU WIN!', xOff + 350, yOff + 200, 40)
            message_display('Click anywhere - next level' , xOff + 350, yOff + 230, 15)
            score = Score + int(bonus)
            if doneyet == False:
                if speed != 1:
                    speed = speed - 1
                doneyet = True
        else:
            message_display('YOU LOSE!', xOff + 350, yOff + 200, 40)
            message_display('Click anywhere to play again.', xOff + 350, yOff + 230, 15)
        message_display("Score", 350,250,35)
        message_display(str(score), 350,300,35)
        pygame.display.update()

        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] == True:
                timer = int(time.time())
                gameState = 0
                X = 25
                Y = 25
                playerX = 0
                playerY = 0
                Score = 0
                Lives = 3
                counter = 0
                valid = 0
                doneyet = False
                bonus = 400
