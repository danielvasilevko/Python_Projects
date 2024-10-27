import random

import numpy as np 

def insert_num(array): #when given an array this function will insert a 2 or 4 randomly at any 0 location
    iterate = range(1,4)
    locations = []
    for i in iterate:          #manually iterate through the board array to find a valid insert location
        for j in iterate:
            if array[i,j] == 0:
                locations.append([i,j])   #add the valid loactions to a list
    
    insert_loc = random.choice(locations)              #chose a rand location       
    insert_num = np.random.choice([2,4],p=[.9,.1])     #chose a number to insert. The different proabilities are needed as those are the actual insert ratios for 2048
    array[insert_loc[0],insert_loc[1]] = insert_num    # replace the chosen 0 location with a number


def game_2048():
    board = np.zeros((4, 4))

    print("W to move up")
    print("S to move down")
    print("A to move left")
    print("D to move right")



board = np.zeros((4, 4)) 

insert_num(board)

print(board)

