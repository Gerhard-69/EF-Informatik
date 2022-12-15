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
        print ('', x, end='')
    print (' ')
    print ('  ', end='')
    #Zahlen seite = y
    for zeile in board:
        for zelle in zeile:
            print(' -', end='')
        print(' ',)
        print (' ', end='')
        y = y+1
        print (y, end='')
        for zelle in zeile:
            print(f'|{zelle}', end='')
        print('|')
        print ('  ', end='')
    for zelle in board[0]:
        print(' -', end='')
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

while True:
    zeilenauswahl = input('Welches Zeile 1-5?')
    spaltenauswahl = input('Welche Spalte 1-5?')
    zeilenauswahl = überprufung(zeilenauswahl)
    spaltenauswahl = überprufung(spaltenauswahl)
    flood_fill(zeilenauswahl, spaltenauswahl, board[zeilenauswahl][spaltenauswahl], ' ')
    board[zeilenauswahl][spaltenauswahl] = ' '
    spielfeld()
    