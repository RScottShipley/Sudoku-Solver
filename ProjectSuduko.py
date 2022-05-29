# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 13:55:45 2019

@author: Scott Shipley

"""
theBoard =[8,0,0,0,0,0,0,0,0,
           0,0,3,6,0,0,0,0,0,
           0,7,0,0,9,0,2,0,0,
           0,5,0,0,0,7,0,0,0,
           0,0,0,0,4,5,7,0,0,
           0,0,0,1,0,0,0,3,0,
           0,0,1,0,0,0,0,6,8,
           0,0,8,5,0,0,0,1,0,
           0,9,0,0,0,0,4,0,0]

blankBoard =[0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0]
"""
Rules:
    1. 1-9 in every row
    2. 1-9 in every column
    3. 1-9 in every box
    3. no repeating numbers in each row, column, or box
"""

def checkMoves(B):
    count = 0
    movesList = []
    while count < len(B):
        if B[count] == 0:
            movesList.append(count)
        count += 1
    return movesList

def legalMove(B, i, n):
    #checks if the move is legal/works     0|1|2     00|01|02
    bo = fitBoard(B)                    #  3|4|5     10|11|12
    col = i%9                           #  6|7|8     20|21|22
    row = i//9
    if n in bo[row]:
        return False
    for m in range(len(bo)):
        if n == bo[m][col]:
            return False
    boxRowStart = row - row%3
    boxColStart = col - col%3
    for checkRow in range(3):
        for column in range(3):
            if n == bo[boxRowStart+checkRow][boxColStart+column]:
                return False
    return True
        
def answer(B = theBoard):
    print("Starting Board:")
    printBoard(B)
    print("Answer Board:")
    M = checkMoves(B)
    def recursionStatement(T = M):
        if len(T) > 0:
            for n in range(1,10):
                if legalMove(B,T[0],n):
                    B[T[0]] = n
                    if recursionStatement(T[1:]):
                        return True
                    B[T[0]] = 0
            return False
        else:
            return True
    if recursionStatement(M):
        return printBoard(B)
    else:
        print("unsolvable")
        return printBoard(B)
    
def fitBoard(B):
    rowBoard = []
    for row in range(0,9):
        holdList = []
        for column in range(0,9):
            holdList.append(B[row*9 + column])
        rowBoard.append(holdList)  
    return rowBoard

def printBoard(B):
    board = fitBoard(B)
    for row in range(9):
        if row % 3 == 0 and row != 0:
                print('______________________')
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print('|',end=" ")
            if col != 8:
                print(board[row][col],end=" ")
            else:
                print(board[row][col])
    
answer()
        
            

            

