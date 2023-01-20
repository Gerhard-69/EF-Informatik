import random
random.seed(2)
numbers = [1, 2, 4, 8]

board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]
def spielfeld(): 
    #Zahlen oben = x
    x = 0
    y = 0 
    print ('  ', end='')
    for i in board:
        x = x+1
        print ('  ', x, end='')
    print (' ')
    print ('   ', end='')
    #Zahlen seite = y
    for zeile in board:
        for zelle in zeile:
            print('----', end='')
        print(' ',)
        print (' ', end='')
        y = y+1
        print (y, end='')
        for zelle in zeile:
            print(f' | {zelle}' , end='')
        print(' |')
        print ('   ', end='')
    for zelle in board[0]:
        print('----', end='')
    print(' ')

spielfeld()

def überprufung(raw, richtung):
    try:
        zahl = int(raw)
        zahl = zahl -1
        if zahl > 5:
            raise
        if zahl <= -1:
            raise
        return zahl
    except:
        print ('Fehlerhafte Eingabe')
        zeilenauswahl = input(f'Welche {richtung} 1-5?')
        zeilenauswahl = überprufung(zeilenauswahl, richtung)
        return zeilenauswahl

def flood_fill(x, y, old, new):
    if x >= len(board) or x == -1:
        return
    if y >= len(board) or y == -1:
        return
    if board[x][y] != old:
        return
    board[x][y] = new
    flood_fill(x+1, y, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x, y+1, old, new)
    flood_fill(x, y-1, old, new)

def leerefelder(c, d, e):
    global leer
    if d >= 5:
        return
    for i in range(4):
        if (board[c][d]) == ' ':
            e = e+1
            leer = e
        c = c-1
    d = d+1
    c = 4
    for i in range(4):
        leerefelder(c, d, e)

def feldverschiebung(a, b):
    zeilen2 = 4
    if b >= 5:
        return
    for i in range (4):
        if (board[a][b]) == ' ':
            a = a-1
            board[zeilen2][b] = board[a][b]
            board[a][b] = ' '
        zeilen2 = zeilen2-1
        a = zeilen2
    if board[a][b] == ' ': #feldauffüllen
        board[a][b] = random.choice(numbers)
    b = b+1
    a = 4
    for i in range(4):
        feldverschiebung(a, b)

def spielende():
    global Gameover
    if board[zeilenauswahl][spaltenauswahl] == 128:
            print ('Sieg')
            Gameover = True

def feldauffüllen():
    if leer > 1:
        board[zeilenauswahl][spaltenauswahl] = save*2
    else:
        board[zeilenauswahl][spaltenauswahl] = save

Gameover = False

while not Gameover:
    zeilenauswahl = input('Welche Zeile 1-5?')
    spaltenauswahl = input('Welche Spalte 1-5?')
    zeilen = 4
    spalten = 0
    leer = 0
    zeilenauswahl = überprufung(zeilenauswahl, 'Zeile')
    spaltenauswahl = überprufung(spaltenauswahl, 'Spalte')
    save = board[zeilenauswahl][spaltenauswahl]
    flood_fill(zeilenauswahl, spaltenauswahl, board[zeilenauswahl][spaltenauswahl], ' ')
    leerefelder(zeilen, spalten, leer)
    feldauffüllen()
    feldverschiebung(zeilen, spalten)
    spielfeld()
    spielende()
