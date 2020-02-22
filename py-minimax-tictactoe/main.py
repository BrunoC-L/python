import tkinter

def getWinner():
    win = 0
    for row in range (0, 3):
        if (board[row][0] == board[row][1] and board[row][0]== board[row][2] and board[row][0] != 0):
            return board[row][0]
    for col in range (0, 3):
        if (board[0][col] == board[1][col] and board[0][col]== board[2][col] and board[0][col] != 0):
            return board[0][col]
    if ((board[0][0] == board[1][1] and board[0][0] == board[2][2] or board[0][2] == board[1][1] and board[0][2] == board[2][0]) and board[1][1] != 0):
        return board[1][1]
    return None

def click(event):
    global movenum
    if (movenum == 9 or getWinner() != None):
        return
    x, y = int(3 * event.x / window.winfo_width()), int(3 * event.y / window.winfo_height())
    if (board[x][y] == 0):
        move(x, y)
        autoMove()

def move(x, y):
    if (x > 2 or x < 0 or y  > 2 or y < 0):
        print("Invalid move lol")
    global movenum
    X(x,y) if (movenum % 2 == 0) else O(x,y)
    movenum += 1

def X(x, y):
    board[x][y] = 1
    canvas.create_line(25 + 100 * x, 25 + 100 * y, 75 + 100 * x, 75 + 100 * y)
    canvas.create_line(25 + 100 * x, 75 + 100 * y, 75 + 100 * x, 25 + 100 * y)

def O(x, y):
    board[x][y] = -1
    canvas.create_oval((25 + 100 * x), (25 + 100 * y), (75 + 100 * x), (75 + 100 * y))

def minimax(maximize):
    global movenum
    if (getWinner() != None):
        return getWinner()
    if (movenum == 9):
        return 0
    if (maximize):
        value = -10
        for x in range(3):
            for y in range(3):
                if (board[x][y] == 0):
                    board[x][y] = 1
                    movenum += 1
                    value = max(value, minimax(False))
                    board[x][y] = 0
                    movenum -= 1
                    if (value == 1):
                        return value
        return value
    else:
        value = 10
        for x in range(3):
            for y in range(3):
                if (board[x][y] == 0):
                    board[x][y] = -1
                    movenum += 1
                    value = min(value, minimax(True))
                    board[x][y] = 0
                    movenum -= 1
                    if (value == -1):
                        return value
        return value
    print("WTF")

def autoMove():
    global movenum
    if (movenum == 9 or getWinner() != None):
        return
    bestValue = 1
    bestX, bestY = -1, -1
    for x in range(3):
        for y in range(3):
            if (board[x][y] == 0):
                if (bestX == -1):
                    bestX = x
                    bestY = y
                board[x][y] = -1
                movenum += 1
                minimaxed = minimax(True)
                board[x][y] = 0
                movenum -= 1
                if (minimaxed < bestValue):
                    bestValue = minimaxed
                    bestX = x
                    bestY = y
                    print("new best at {},{}".format(x,y))
                if (bestValue == -1):
                    move(x, y)
                    print("-1 found at {},{}".format(x,y))
                    return
    move(bestX, bestY)
    print("0 found at {},{}".format(bestX,bestY))


window = tkinter.Tk('Tic Tac Toe')
canvas = tkinter.Canvas(window, width = 300, height = 300)
canvas.pack()
canvas.create_line(000, 100, 300, 100)
canvas.create_line(000, 200, 300, 200)
canvas.create_line(100, 000, 100, 300)
canvas.create_line(200, 000, 200, 300)
window.maxsize(300, 300)
window.minsize(300, 300)

window.bind("<Button 1>", click)
window.bind("<Button 2>", click)

movenum = 0

board = [
    [ 1, 0, 0],
    [ 0, 0, 0],
    [ 0,-1, 0],
]

print(minimax(True))
print(minimax(False))

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

window.mainloop()