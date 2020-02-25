def getWinner():
    if ((board[0][0]==board[1][1] and board[0][0]==board[2][2] or board[0][2]==board[1][1] and board[0][2]==board[2][0]) and board[1][1]!=0): return board[1][1]
    for rowOrCol in range(3):
        if (board[rowOrCol][0]==board[rowOrCol][1] and board[rowOrCol][0]==board[rowOrCol][2] and board[rowOrCol][0]!=0): return board[rowOrCol][0]
        if (board[0][rowOrCol]==board[1][rowOrCol] and board[0][rowOrCol]==board[2][rowOrCol] and board[0][rowOrCol]!=0): return board[0][rowOrCol]

def click(event):
    if (movenum == 9 or getWinner() != None): return
    x, y = int(3 * event.x / window.winfo_width()), int(3 * event.y / window.winfo_height())
    if (board[x][y] == 0):
        move(x, y)
        autoMove()

def move(x, y):
    print(x,y)
    global movenum
    X(x,y) if (movenum % 2 == 0) else O(x,y)
    movenum += 1

def X(x, y):
    board[x][y] = 1
    canvas.create_line(50 + 200 * x, 50 + 200 * y, 150 + 200 * x, 150 + 200 * y)
    canvas.create_line(50 + 200 * x, 150 + 200 * y, 150 + 200 * x, 50 + 200 * y)

def O(x, y):
    board[x][y] = -1
    canvas.create_oval((50 + 200 * x), (50 + 200 * y), (150 + 200 * x), (150 + 200 * y))

def minimax():
    global movenum
    if (getWinner() != None): return getWinner()
    elif (movenum == 9): return 0
    maximize = movenum % 2 == 0
    value = -10 if maximize else 10
    for x in range(3):
        for y in range(3):
            if (board[x][y] == 0):
                board[x][y] = 1 if maximize else -1
                movenum += 1
                minimaxed = minimax()
                value = max(value, minimaxed) if maximize else min(value, minimaxed)
                board[x][y] = 0
                movenum -= 1
                if (value > 0 and maximize or value < 0 and not maximize): return value
    return value

def autoMove():
    global movenum
    if (movenum == 9 or getWinner() != None): return
    maximize = movenum % 2 == 0
    bestValue, bestX, bestY = -1 if maximize else 1 , -1, -1
    for x in range(3):
        for y in range(3):
            if (board[x][y] == 0):
                if (bestX == -1):
                    bestX = x
                    bestY = y
                board[x][y] = 1 if maximize else -1
                movenum += 1
                minimaxed = minimax()
                board[x][y] = 0
                movenum -= 1
                if (maximize and minimaxed > bestValue or not maximize and minimaxed < bestValue):
                    bestValue = minimaxed
                    bestX = x
                    bestY = y
    move(bestX, bestY)

import tkinter
window = tkinter.Tk('Tic Tac Toe')
canvas = tkinter.Canvas(window, width = 600, height = 600)
canvas.pack()
canvas.create_line(000, 200, 600, 200)
canvas.create_line(000, 400, 600, 400)
canvas.create_line(200, 000, 200, 600)
canvas.create_line(400, 000, 400, 600)
window.bind("<Button 1>", click)
movenum = 0
board =[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
window.mainloop()