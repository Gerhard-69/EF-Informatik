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
            raise 'Zu grosse Zahl'
        return zahl
    except:
        print ('Fehlerhafte Eingabe')
        zeilenauswahl = input('Welches Zeile 1-5?')
        spaltenauswahl = input('Welche Spalte 1-5?')
        zeilenauswahl = überprufung(zeilenauswahl)
        spaltenauswahl = überprufung(spaltenauswahl)

while True:
    zeilenauswahl = input('Welches Zeile 1-5?')
    spaltenauswahl = input('Welche Spalte 1-5?')
    zeilenauswahl = überprufung(zeilenauswahl)
    spaltenauswahl = überprufung(spaltenauswahl)
    board[zeilenauswahl-1][spaltenauswahl-1] = ' '
    spielfeld()