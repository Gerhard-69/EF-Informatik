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

def überprufung(raw):
    try:
        zahl = int(raw)
        zahl = zahl -1
        if zahl > 5:
            raise
        return zahl
    except:
        print ('Fehlerhafte Eingabe')
        zeilenauswahl = input('Welches Zeile 1-5?')
        spaltenauswahl = input('Welche Spalte 1-5?')
        zeilenauswahl = überprufung(zeilenauswahl)
        spaltenauswahl = überprufung(spaltenauswahl)

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

def feldverschiebung(a, b):
    zeilen2 = 4
    if b >= 5:
        return
    if a <= -1:
        return
    for i in range (4):
        if (board[a-1][b]) == ' ':
            a = a-2
            if a <= -1:
                return
            if (board[a][b]) == ' ':
                a = a-1
                if a <= -1:
                    return
                if (board[a][b]) == ' ':
                    a = a-1
                    if a <= -1:
                        return
            board[zeilen2][b] = board[a][b]
            board[a][b] = ' '
            a = zeilen2
        zeilen2 = zeilen2-1
    b = b+1
    for i in range(4):
        feldverschiebung(a, b)
def feldauffüllung(c, d):
    if d >= 5:
        return
    if c <= -1:
        return

while True:
    zeilenauswahl = input('Welches Zeile 1-5?')
    spaltenauswahl = input('Welche Spalte 1-5?')
    zeilen = 5
    spalten = 0
    zeilenauswahl = überprufung(zeilenauswahl)
    spaltenauswahl = überprufung(spaltenauswahl)
    save = board[zeilenauswahl][spaltenauswahl]
    flood_fill(zeilenauswahl, spaltenauswahl, board[zeilenauswahl][spaltenauswahl], ' ')
    board[zeilenauswahl][spaltenauswahl] = save*2
    feldverschiebung(zeilen, spalten)
    feldauffüllung
    spielfeld()
    