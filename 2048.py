import random

import numpy as np 

def insert_num(array): #when given an array this function will insert a 2 or 4 randomly at any 0 location
    iterate = range(1,4)
    locations = []
    for i in iterate:
        for j in iterate:
            if array[i,j] == 0:
                locations.append([i,j])
    
    insert_loc = random.choice(locations)
    print(insert_loc)


def game_2048():
    print("W to move up")
    print("S to move down")
    print("A to move left")
    print("D to move right")

board = np.zeros((4, 4)) 

insert_num(board)

