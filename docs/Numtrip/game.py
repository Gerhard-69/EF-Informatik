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
        if zahl > 5:
            raise
        return zahl
    except:
        print ('Fehlerhafte Eingabe')
        zeilenauswahl = input('Welches Zeile 1-5?')
        spaltenauswahl = input('Welche Spalte 1-5?')
        zeilenauswahl = überprufung(zeilenauswahl)
        spaltenauswahl = überprufung(spaltenauswahl)

def flood_fill(x ,y, old, new):
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
        return
    # secondly, check if the current position equals the old value
    if board[y][x] != old:
        return
    # thirdly, set the current position to the new value
    board[y][x] = new
    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x, y+1, old, new)
    flood_fill(x, y-1, old, new)

while True:
    zeilenauswahl = input('Welches Zeile 1-5?')
    spaltenauswahl = input('Welche Spalte 1-5?')
    zeilenauswahl = überprufung(zeilenauswahl)
    spaltenauswahl = überprufung(spaltenauswahl)
    flood_fill(zeilenauswahl, spaltenauswahl, board[zeilenauswahl-1][spaltenauswahl-1], ' ')
    board[zeilenauswahl-1][spaltenauswahl-1] = ' '
    spielfeld()
    