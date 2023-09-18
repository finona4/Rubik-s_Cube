# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:35:43 2023

@author: fiona
"""
import random

"""
random array for each face, total 9 sq for each col (3x3 cube)
user inputs which face row/col to turn, which direction
turns
play until win or quit
"""
"""
if user asks comp to solve
comp takes its turns until solved
"""

def createCube():
    """
    Creates a 3x3 Rubik's cube, each face with its own array.

    Returns
    -------
    cube = all faces of the cube in a tuple (front, top, back, bottom, right, left).

    """
    front = [["/" for x in range(3)] for y in range(3)]
    top = [["/" for x in range(3)] for y in range(3)]
    back = [["/" for x in range(3)] for y in range(3)]
    bottom = [["/" for x in range(3)] for y in range(3)]
    right = [["/" for x in range(3)] for y in range(3)]
    left = [["/" for x in range(3)] for y in range(3)]
    cube = (front, top, back, bottom, right, left)
    
    blue = 9
    red = 9
    yellow = 9
    white = 9
    green = 9
    orange = 9
    
    #for blue
    cube = blueSpots(blue, cube[0], cube[1], cube[2], cube[3], cube[4], cube[5])
    #for red
    cube = redSpots(red, cube[0], cube[1], cube[2], cube[3], cube[4], cube[5])
    #for yellow
    cube = yellowSpots(yellow, cube[0], cube[1], cube[2], cube[3], cube[4], cube[5])
    #for white
    cube = whiteSpots(white, cube[0], cube[1], cube[2], cube[3], cube[4], cube[5])
    #for green
    cube = greenSpots(green, cube[0], cube[1], cube[2], cube[3], cube[4], cube[5])
    #for orange
    cube = orangeSpots(orange, cube[0], cube[1], cube[2], cube[3], cube[4], cube[5])
    
    return cube

def blueSpots(blue, front, top, back, bottom, right, left):
    while (not blue == 0):
        #randomly determine which face
        face = random.randint(1,6)
        numFreeSpots = 0
        #for front
        if (face==1):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(front)):
                for c in range(len(front[0])):
                    if (front[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not front[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                front[spot[0]][spot[1]] = "B"
        #for top
        elif (face==2):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(top)):
                for c in range(len(top[0])):
                    if (top[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not top[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                top[spot[0]][spot[1]] = "B"
        #for back
        elif (face==3):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(back)):
                for c in range(len(back[0])):
                    if (back[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not back[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                back[spot[0]][spot[1]] = "B"
        #for bottom
        elif (face==4):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(bottom)):
                for c in range(len(bottom[0])):
                    if (bottom[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not bottom[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                bottom[spot[0]][spot[1]] = "B"   
        #for right
        elif (face==5):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(right)):
                for c in range(len(right[0])):
                    if (right[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not right[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                right[spot[0]][spot[1]] = "B"
        #for left
        elif (face==6):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(left)):
                for c in range(len(left[0])):
                    if (left[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not left[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                left[spot[0]][spot[1]] = "B"

        if (numFreeSpots!=0):    
            blue -= 1
        
    return (front, top, back, bottom, right, left)
            
def redSpots(red, front, top, back, bottom, right, left):
    while (not red == 0):
        #randomly determine which face
        face = random.randint(1,6)
        numFreeSpots = 0
        #for front
        if (face==1):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(front)):
                for c in range(len(front[0])):
                    if (front[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not front[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                front[spot[0]][spot[1]] = "R"
        #for top
        elif (face==2):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(top)):
                for c in range(len(top[0])):
                    if (top[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not top[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                top[spot[0]][spot[1]] = "R"
        #for back
        elif (face==3):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(back)):
                for c in range(len(back[0])):
                    if (back[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not back[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                back[spot[0]][spot[1]] = "R"
        #for bottom
        elif (face==4):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(bottom)):
                for c in range(len(bottom[0])):
                    if (bottom[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not bottom[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                bottom[spot[0]][spot[1]] = "R"  
        #for right
        elif (face==5):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(right)):
                for c in range(len(right[0])):
                    if (right[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not right[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                right[spot[0]][spot[1]] = "R"
        #for left
        elif (face==6):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(left)):
                for c in range(len(left[0])):
                    if (left[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not left[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                left[spot[0]][spot[1]] = "R"

        if (numFreeSpots!=0): 
            red -= 1
        
    return (front, top, back, bottom, right, left)

def yellowSpots(yellow, front, top, back, bottom, right, left):
    while (not yellow == 0):
        #randomly determine which face
        face = random.randint(1,6)
        numFreeSpots = 0
        #for front
        if (face==1):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(front)):
                for c in range(len(front[0])):
                    if (front[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not front[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                front[spot[0]][spot[1]] = "Y"
        #for top
        elif (face==2):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(top)):
                for c in range(len(top[0])):
                    if (top[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not top[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                top[spot[0]][spot[1]] = "Y"
        #for back
        elif (face==3):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(back)):
                for c in range(len(back[0])):
                    if (back[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not back[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                back[spot[0]][spot[1]] = "Y"
        #for bottom
        elif (face==4):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(bottom)):
                for c in range(len(bottom[0])):
                    if (bottom[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not bottom[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                bottom[spot[0]][spot[1]] = "Y" 
        #for right
        elif (face==5):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(right)):
                for c in range(len(right[0])):
                    if (right[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not right[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                right[spot[0]][spot[1]] = "Y"
        #for left
        elif (face==6):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(left)):
                for c in range(len(left[0])):
                    if (left[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not left[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                left[spot[0]][spot[1]] = "Y"
            
        if (numFreeSpots!=0):     
            yellow -= 1
        
    return (front, top, back, bottom, right, left)
    
def whiteSpots(white, front, top, back, bottom, right, left):
    while (not white == 0):
        #randomly determine which face
        face = random.randint(1,6)
        numFreeSpots = 0
        #for front
        if (face==1):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(front)):
                for c in range(len(front[0])):
                    if (front[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not front[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                front[spot[0]][spot[1]] = "W"
        #for top
        elif (face==2):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(top)):
                for c in range(len(top[0])):
                    if (top[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not top[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                top[spot[0]][spot[1]] = "W"
        #for back
        elif (face==3):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(back)):
                for c in range(len(back[0])):
                    if (back[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not back[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                back[spot[0]][spot[1]] = "W"
        #for bottom
        elif (face==4):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(bottom)):
                for c in range(len(bottom[0])):
                    if (bottom[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not bottom[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                bottom[spot[0]][spot[1]] = "W"
        #for right
        elif (face==5):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(right)):
                for c in range(len(right[0])):
                    if (right[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not right[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                right[spot[0]][spot[1]] = "W"
        #for left
        elif (face==6):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(left)):
                for c in range(len(left[0])):
                    if (left[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not left[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                left[spot[0]][spot[1]] = "W"

        if (numFreeSpots!=0):     
            white -= 1
        
    return (front, top, back, bottom, right, left)

def greenSpots(green, front, top, back, bottom, right, left):
    while (not green == 0):
        #randomly determine which face (can't be full already)
        face = random.randint(1,6)
        numFreeSpots = 0
        #for front
        if (face==1):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(front)):
                for c in range(len(front[0])):
                    if (front[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not front[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                front[spot[0]][spot[1]] = "G"
        #for top
        elif (face==2):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(top)):
                for c in range(len(top[0])):
                    if (top[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not top[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                top[spot[0]][spot[1]] = "G"
        #for back
        elif (face==3):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(back)):
                for c in range(len(back[0])):
                    if (back[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not back[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                back[spot[0]][spot[1]] = "G"
        #for bottom
        elif (face==4):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(bottom)):
                for c in range(len(bottom[0])):
                    if (bottom[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not bottom[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                bottom[spot[0]][spot[1]] = "G" 
        #for right
        elif (face==5):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(right)):
                for c in range(len(right[0])):
                    if (right[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not right[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                right[spot[0]][spot[1]] = "G"
        #for left
        elif (face==6):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(left)):
                for c in range(len(left[0])):
                    if (left[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not left[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                left[spot[0]][spot[1]] = "G"

        if (numFreeSpots!=0):     
            green -= 1
        
    return (front, top, back, bottom, right, left)
        
def orangeSpots(orange, front, top, back, bottom, right, left):
    while (not orange == 0):
        #randomly determine which face
        face = random.randint(1,6)
        numFreeSpots = 0
        #for front
        if (face==1):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(front)):
                for c in range(len(front[0])):
                    if (front[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not front[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                front[spot[0]][spot[1]] = "O"
        #for top
        elif (face==2):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(top)):
                for c in range(len(top[0])):
                    if (top[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not top[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                top[spot[0]][spot[1]] = "O"
        #for back
        elif (face==3):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(back)):
                for c in range(len(back[0])):
                    if (back[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not back[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                back[spot[0]][spot[1]] = "O"
        #for bottom
        elif (face==4):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(bottom)):
                for c in range(len(bottom[0])):
                    if (bottom[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not bottom[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                bottom[spot[0]][spot[1]] = "O"  
        #for right
        elif (face==5):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(right)):
                for c in range(len(right[0])):
                    if (right[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not right[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                right[spot[0]][spot[1]] = "O"
        #for left
        elif (face==6):
            #randomly determine which spot to put blue (can't be full already)
            for r in range(len(left)):
                for c in range(len(left[0])):
                    if (left[r][c]=='/'):
                        numFreeSpots += 1
            if (numFreeSpots!=0):
                spot = (random.randint(0,2), random.randint(0,2))
                while (not left[spot[0]][spot[1]] == '/'):
                    spot = (random.randint(0,2), random.randint(0,2))
                left[spot[0]][spot[1]] = "O"

        if (numFreeSpots!=0):     
            orange -= 1
        
    return (front, top, back, bottom, right, left)

def printCube(cube):
    """
    Print the cube
    
    """
    print("\t\t\t Top")
    for r in range(len(cube[1][0])):
        print("\t\t\t",cube[1][r])
    print("Left\t\t\t Front\t\t\t Right")
    for r in range(len(cube[5][0])):
        print(cube[5][r] ,"\t", cube[0][r] ,"\t", cube[4][r])
    print("\t\t\t Bottom")
    for r in range(len(cube[3][0])):
        print("\t\t\t",cube[3][r])
    print("\t\t\t Back")
    for r in range(len(cube[2][0])):
        print("\t\t\t", cube[2][r])

def userInput():
    """
    Performs actions relating to recieving and validating user input.

    Returns
    -------
    the respective user input

    """
    print("0=front, 1=top, 2=back, 3=bottom, 4=right, 5=left")
    print("q to quit, comp to let computer solve")
    face = input("Which face would you like to focus on? ")
    #quit or computer
    if (face=='q'):
        return 'q'
    elif (face=='comp'):
        return "comp"
    #get the face
    while (not face.isnumeric() or (int(face)<0 or int(face)>5)):
        print("Invalid input.")
        face = input("Which face would you like to focus on? ")
    face = int(face)
    #get row/col
    rowcol = input("Enter r for moving a row, c for moving a column. ")
    while (not rowcol=="r" and not rowcol=="c"):
        print("Invalid input.")
        rowcol = input("Enter r for moving a row, c for moving a column. ")
    #get row/col num
    rowcolNum = input("Enter which row/column you want to move (0-2). ")
    while (not rowcolNum.isnumeric() or (int(rowcolNum)<0 or int(rowcolNum)>2)):
        print("Invalid input.")
        rowcolNum = input("Enter which row/column you want to move. (0-2) ")
    rowcolNum = int(rowcolNum)
    #get direction
    dir = input("Which direction do you want to move the row/column? (up/down for col, left/right for row) ")
    while (not(dir=="up" or dir=="down" or dir=="left" or dir=="right") or (rowcol=="r" and (dir=="up" or dir=="down")) or (rowcol=="c" and(dir=="left" or dir=="right"))):
        print("Invalid input.")
        dir = input("Which direction do you want to move the row/column? (up/down for col, left/right for row) ")

    return (face, rowcol, rowcolNum, dir)
    
def userTurn(turnParam, cube):
    """
    Turns the cube according to how the user requested.

    Returns
    -------
    the updated cube
    
    """
    #separate the turnParam into the parameters
    face = turnParam[0] #int
    rowcol = turnParam[1]   #str
    rowcolNum = turnParam[2]    #int
    dir = turnParam[3]  #str
    
    #if dealing w rows
    if (rowcol == 'r'):
        #move that row to the right/left for all faceCurr, 'left', 'right' faces
        if (face == 0 or face == 2 or face == 4 or face == 5):
            face1 = 0
            face2 = 4
            face3 = 2
            face4 = 5
            face5 = 1
            face6 = 3
        elif (face == 1 or face == 3):
            face1 = 1
            face2 = 4
            face3 = 3
            face4 = 5
            face5 = 0
            face6 = 2
        #vars for each row to be switched
        row1 = cube[face1][rowcolNum]
        row2 = cube[face2][rowcolNum]
        row3 = cube[face3][rowcolNum]
        row4 = cube[face4][rowcolNum]
        #vars for rotating 'top'/'bottom' if needed
        if (rowcolNum == 0):
            rotCol0 = [cube[face5][0][0], cube[face5][1][0], cube[face5][2][0]]
            rotCol1 = [cube[face5][0][1], cube[face5][1][1], cube[face5][2][1]]
            rotCol2 = [cube[face5][0][2], cube[face5][1][2], cube[face5][2][2]]
        elif (rowcolNum == 2):
            rotCol0 = [cube[face6][2][0], cube[face6][1][0], cube[face6][0][0]]
            rotCol1 = [cube[face6][2][1], cube[face6][1][1], cube[face6][0][1]]
            rotCol2 = [cube[face6][2][2], cube[face6][1][2], cube[face6][0][2]]

        #switch rows
        #rotate the 'top'/'bottom' faces cw/anti-cw if its a top/bottom row
        if (dir=="right"):
            #move rows right
            cube[face1][rowcolNum] = row4
            cube[face2][rowcolNum] = row1
            cube[face3][rowcolNum] = row2
            cube[face4][rowcolNum] = row3
            #rotate 'top'/'bottom' anti-/cw if needed
            if (rowcolNum == 0):
                #anti
                cube[face5][0] = rotCol2
                cube[face5][1] = rotCol1
                cube[face5][2] = rotCol0
            elif (rowcolNum == 2):
                #cw
                cube[face6][0] = rotCol0
                cube[face6][1] = rotCol1
                cube[face6][2] = rotCol2
                
        elif (dir=="left"):
            #move rows left
            cube[face1][rowcolNum] = row2
            cube[face2][rowcolNum] = row3
            cube[face3][rowcolNum] = row4
            cube[face4][rowcolNum] = row1
            #rotate 'top'/'bottom' anti-/cw if needed
            if (rowcolNum == 0):
                #cw
                cube[face5][0] = rotCol0
                cube[face5][1] = rotCol1
                cube[face5][2] = rotCol2
            elif (rowcolNum == 2):
                #anti
                cube[face6][0] = rotCol2
                cube[face6][1] = rotCol1
                cube[face6][2] = rotCol0
    
    #if dealing with columns
    if (rowcol=='c'):
        #move that column up/down for all faceCurr, 'top', 'bottom' faces
        if (face == 0 or face == 1 or face == 2 or face == 3):
            face1 = 0
            face2 = 1
            face3 = 2
            face4 = 3
            face5 = 5
            face6 = 4
        elif (face == 4 or face == 5):
            face1 = 4
            face2 = 1
            face3 = 5
            face4 = 3
            face5 = 0
            face6 = 2
        #vars for each col to be switched
        col1 = [cube[face1][0][rowcolNum], cube[face1][1][rowcolNum], cube[face1][2][rowcolNum]]
        col2 = [cube[face2][0][rowcolNum], cube[face2][1][rowcolNum], cube[face2][2][rowcolNum]]
        col3 = [cube[face3][0][rowcolNum], cube[face3][1][rowcolNum], cube[face3][2][rowcolNum]]
        col4 = [cube[face4][0][rowcolNum], cube[face4][1][rowcolNum], cube[face4][2][rowcolNum]]
        #vars for rotating 'right'/'left' if needed
        if (rowcolNum == 0):
            rotCol0 = [cube[face5][0][0], cube[face5][1][0], cube[face5][2][0]]
            rotCol1 = [cube[face5][0][1], cube[face5][1][1], cube[face5][2][1]]
            rotCol2 = [cube[face5][0][2], cube[face5][1][2], cube[face5][2][2]]
        elif (rowcolNum == 2):
            rotCol0 = [cube[face6][2][0], cube[face6][1][0], cube[face6][0][0]]
            rotCol1 = [cube[face6][2][1], cube[face6][1][1], cube[face6][0][1]]
            rotCol2 = [cube[face6][2][2], cube[face6][1][2], cube[face6][0][2]]

        #switch cols
        #rotate the 'right'/'left' faces cw/anti-cw if its a right/left col
        if (dir=="up"):
            #move cols up
            [cube[face1][0][rowcolNum], cube[face1][1][rowcolNum], cube[face1][2][rowcolNum]] = col4
            [cube[face2][0][rowcolNum], cube[face2][1][rowcolNum], cube[face2][2][rowcolNum]] = col1
            [cube[face3][0][rowcolNum], cube[face3][1][rowcolNum], cube[face3][2][rowcolNum]] = col2
            [cube[face4][0][rowcolNum], cube[face4][1][rowcolNum], cube[face4][2][rowcolNum]] = col3
            #rotate 'right'/'left' anti-/cw if needed
            if (rowcolNum == 0):
                #anti
                cube[face5][0] = rotCol2
                cube[face5][1] = rotCol1
                cube[face5][2] = rotCol0
            elif (rowcolNum == 2):
                #cw
                cube[face6][0] = rotCol0
                cube[face6][1] = rotCol1
                cube[face6][2] = rotCol2

        elif (dir=="down"):
            #move cols down
            [cube[face1][0][rowcolNum], cube[face1][1][rowcolNum], cube[face1][2][rowcolNum]] = col2
            [cube[face2][0][rowcolNum], cube[face2][1][rowcolNum], cube[face2][2][rowcolNum]] = col3
            [cube[face3][0][rowcolNum], cube[face3][1][rowcolNum], cube[face3][2][rowcolNum]] = col4
            [cube[face4][0][rowcolNum], cube[face4][1][rowcolNum], cube[face4][2][rowcolNum]] = col1
            #rotate 'right'/'left' anti-/cw if needed
            if (rowcolNum == 0):
                #cw
                cube[face5][0] = rotCol0
                cube[face5][1] = rotCol1
                cube[face5][2] = rotCol2
            elif (rowcolNum == 2):
                #anti
                cube[face6][0] = rotCol2
                cube[face6][1] = rotCol1
                cube[face6][2] = rotCol0
        
    printCube(cube)
    
def compTurn(cube):
    """
    The computer solves the cube turn-by-turn

    Returns
    -------
    the updated cube
    """
def checkBestCross(cube):
    """
    Checks which face to start the first cross on

    Returns
    -------
    the face number
    """ 
def fourMoves(cube, face, side):
    """
    Performs the 4 moves that are used often (up, left/right, down, right/left)

    Returns
    -------
    the updated cube
    """


def checkWon(cube):
    #check if top, bottom, and front/left/right are solved
    count1 = 0  #for top
    color1 = cube[1][0][0]
    count2 = 0  #for bottom
    color2 = cube[3][0][0]
    count3 = 0  #for front
    color3 = cube[0][0][0]

    for r in range(len(cube[0])):
        #count all the pieces in the faces that are one color
        for p in range(len(cube[0][r])):
            if (cube[1][r][p] == color1):
                count1 += 1
            if (cube[3][r][p] == color2):
                count2 += 1
            if (cube[0][r][p] == color3):
                count3 += 1

    #if those faces are solved, the cube is solved
    if (count1 == 9 and count2 == 9 and count3 == 9):
        won = True
    else:
        won = False

    return won


#create the cube
cube = createCube()
print("The cube has been scrambled.")
printCube(cube)
won = False
turnParam = userInput()

#play until the user quits or wants the computer to solve
while(not turnParam=='q' and not turnParam=="comp" and not won):
    cube = userTurn(turnParam, cube)
    printCube(cube)
    won = checkWon(cube)
    if (not won):
        turnParam = userInput()

if (won):
    print("You figured it out!")
elif (turnParam == "comp"):
    while (not won):
        cube = compTurn(cube)
        printCube(cube)
        won = checkWon(cube)
print("Thanks for playing.")