#!/usr/bin/env python
"""tictactoe.py

A Simple tic tac toe game
"""

#Introduce the game
print "Welcome to Tic-Tac-Toe."
print "Input a row then a column separated by a single space."

# Implement a version of tic tac toe
player = 1
board = [ 0 for _ in range(9) ]
win = False
c = ["O", " ", "X"]

while not win:
    # display board
    print "   1 2 3 "
    print "1 [%s]" % "|".join(c[i+1] for i in board[0:3])
    print "2 [%s]" % "|".join(c[i+1] for i in board[3:6])
    print "3 [%s]" % "|".join(c[i+1] for i in board[6:9])

    # get input
    y, x = [ int(x) - 1 for x in raw_input("Player %s:  " % c[player+1]).split() ]
    pos = x + (y*3)

    # updates board
    if board[pos] == 0:
        board[pos] += player
        player = -player
    else:
        print "ERROR 1"

    # test for win
    solved = []
    #rows
    solved.append(sum(board[0:3]))
    solved.append(sum(board[3:6]))
    solved.append(sum(board[6:9]))
    #columns
    solved.append(sum(board[0::3]))
    solved.append(sum(board[1::3]))
    solved.append(sum(board[2::3]))
    #diagonals
    solved.append(sum(board[0::4]))
    solved.append(sum(board[2:8:2]))
    win = any(w for w in solved if abs(w) == 3)

# print win statement
player = -player

# display board                                                                                        
print "   1 2 3 "
print "1 [%s]" % "|".join(c[i+1] for i in board[0:3])
print "2 [%s]" % "|".join(c[i+1] for i in board[3:6])
print "3 [%s]" % "|".join(c[i+1] for i in board[6:9])

print "Player %s wins!!!11!" % c[player+1]
