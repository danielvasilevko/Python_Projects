# This is a python version of the classic game 2048. The main gameplay loop is to shift around numbers which merge together to create larger ones.
# The game end when (as the title suggests) you reach 2048. 

import random

import numpy as np 

def insert_num(array): #when given an array this function will insert a 2 or 4 randomly at any 0 location
    iterate = range(0,4)
    locations = []
    for i in iterate:          #manually iterate through the board array to find a valid insert location
        for j in iterate:
            if array[i,j] == 0:
                locations.append([i,j])   #add the valid loactions to a list
    
    if not locations:                                  #if there are no locations for 0's to go you lose
        return("Lose")
    insert_loc = random.choice(locations)              #chose a rand location       
    insert_num = np.random.choice([2,4],p=[.9,.1])     #chose a number to insert. The different proabilities are needed as those are the actual insert ratios for 2048
    array[insert_loc[0],insert_loc[1]] = insert_num    #replace the chosen 0 location with a number

def press_W(array):
    iterate = range(0,4)
    point = 0
    for i in iterate:         
        for j in iterate:
            if array[i,j] == 0 or i ==0:
                continue
            else:
                if array[i-1,j] == 0:                   #case for a number just moving up
                    array[i-1,j] = array[i,j]
                    array[i,j] = 0
                elif array[i-1,j] == array[i,j]:        #case for 2 numbers merging
                    array[i-1,j] = array[i-1,j] * 2
                    array[i,j] = 0
                    point += int(array[i-1,j])
                else: 
                    continue
    return(array,point)

def press_S(array):
    iterate = range(3,-1,-1)
    point = 0
    for i in iterate:         
        for j in iterate:
            if array[i,j] == 0 or i ==3:    
                continue
            else:
                if array[i+1,j] == 0:                   #case for a number just moving up
                    array[i+1,j] = array[i,j]
                    array[i,j] = 0
                elif array[i+1,j] == array[i,j]:        #case for 2 numbers merging
                    array[i+1,j] = array[i+1,j] * 2
                    array[i,j] = 0
                    point += int(array[i+1,j])
                else: 
                    continue  
    return(array,point)   

def press_d(array):
    iterate = range(3,-1,-1)
    point = 0
    for i in iterate:         
        for j in iterate:
            if array[j,i] == 0 or i ==3:    
                continue
            else:
                if array[j,i+1] == 0:                   #case for a number just moving up
                    array[j,i+1] = array[j,i]
                    array[j,i] = 0
                elif array[j,i+1] == array[j,i]:        #case for 2 numbers merging
                    array[j,i+1] = array[j,i+1] * 2
                    array[j,i] = 0
                    point += int(array[j,i+1])
                else: 
                    continue  
    return(array,point)   
   

def press_a(array):
    iterate = range(0,4)
    point = 0
    for i in iterate:         
        for j in iterate:
            if array[j,i] == 0 or i ==0:
                continue
            else:
                if array[j,i-1] == 0:                   #case for a number just moving up
                    array[j,i-1] = array[j,i]
                    array[j,i] = 0
                elif array[j,i-1] == array[j,i]:        #case for 2 numbers merging
                    array[j,i-1] = array[j,i-1] * 2
                    array[j,i] = 0
                    point += int(array[j,i-1])
                else: 
                    continue
    return(array,point)   


def game_2048():
    
    board = np.zeros((4, 4))
    insert_num(board)
    insert_num(board)

    print("W to move up")
    print("S to move down")
    print("A to move left")
    print("D to move right")
    
    print(board)
    game_winner = False                  
    gamekiller =True
    points = 0

    winner_amount = 2048

    while gamekiller == True:
        print(f"Points:{points}")
        move = input("Chose a move. ").lower()
        if move == "w":
            old_board = board.copy()
            new_board = np.empty((4,4))
            while np.array_equal(old_board,new_board) == False:   #keeps doing press_W until the board cannot change aka is in its final positino
                new_board = old_board.copy()
                old_board,temppoints = press_W(old_board)   #collects the new board state and the points from merges
                if temppoints == winner_amount:             #if 2048 points are gotten from 1 merge then 2048 must exist on the board so the person wins
                    game_winner = True
                points += temppoints                 
            board = new_board.copy()
    
        elif move == "s":
            old_board = board.copy()
            new_board = np.empty((4,4))
            while np.array_equal(old_board,new_board) == False:
                new_board = old_board.copy()
                old_board,temppoints = press_S(old_board)             
                if temppoints == winner_amount:
                    game_winner = True
                points += temppoints
            board = new_board.copy()
        
        elif move == "d":
            old_board = board.copy()
            new_board = np.empty((4,4))
            while np.array_equal(old_board,new_board) == False:
                new_board = old_board.copy()
                old_board,temppoints = press_d(old_board)
                if temppoints == winner_amount:
                    game_winner = True
                points += temppoints
            board = new_board.copy()
        
        elif move == "a":
            old_board = board.copy()
            new_board = np.empty((4,4))
            while np.array_equal(old_board,new_board) == False:
                new_board = old_board.copy()
                old_board,temppoints = press_a(old_board)
                if temppoints == winner_amount:
                    game_winner = True
                points += temppoints
            board = new_board.copy()
        else:
            print("Invalid choice. Try Again")
            continue
        

        if insert_num(board) == "Lose":
            gamekiller = False
    
        print(board)
        if game_winner == True:
            print("CONGRATULATIONS! YOU WON!")

    again = input("Sorry, you lost. Type Yes to play again. ")
    if again == "Yes":
        game_2048()
    
game_2048()
