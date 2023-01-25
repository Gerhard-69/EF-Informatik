import random
random.seed(2)
numbers = [1, 2, 4, 8] # bestimmt die zahlen die zufällig ausgewählt werden

board = [
        [random.choice(numbers),random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)],
        [random.choice(numbers),random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)],
        [random.choice(numbers),random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)],
        [random.choice(numbers),random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)],
        [random.choice(numbers),random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)]
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
            if zelle > 10:
                print(f' |{zelle}' , end='')
            else:
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
    if d >= len(board):
        return
    for i in range(5):
        if (board[c][d]) == ' ':
            e = e+1
            leer = e
        c = c-1
    d = d+1
    c = 4
    for i in range(4):
        leerefelder(c, d, e)

def feldverschiebung(a, b):
    d = 0 # d beschreibt ob ein grösserer Sprung schon gemacht wurde.
    zeilen2 = 4 # merkt sich Zeile in der ich mich befinde
    if b >= len(board):
        return
    for i in range (4):
        if (board[a][b]) == ' ':
            if a-2 > -1: # wenn a < 0 wäre würde ich wieder unten im Feld landen. mit diesem if verhindere ich es
                if (board[a-1][b]) == ' ': # ist das feld über dem leeren feld auch leer? (zwei hintereinander)
                    board[zeilen2][b] = board[a-2][b]
                    board[a-2][b] = ' '
                    if board[a][b] == ' ': # wenn das feld immer noch leer ist
                        d = d + 1
                    if d == 1: # wenn das feld nicht mehr leer ist würden die nächsten zeilen code alles zerstören
                        if a-3 > -1:
                            if (board[a-2][b]) == ' ':
                                board[zeilen2][b] = board[a-3][b]
                                board[a-3][b] = ' '
                                if board[a][b] == ' ': # wenn das feld immer noch leer ist
                                    d = d + 1
                                if d == 2: # wenn das feld nicht mehr leer ist würden die nächsten zeilen code alles zerstören
                                    if a-4 > -1:
                                        if (board[a-3][b]) == ' ':
                                            board[zeilen2][b] = board[a-4][b]
                                            board[a-4][b] = ' '
            if (board[a][b]) == ' ': # ist das feld immernoch leer
                board[zeilen2][b] = board[a-1][b]
                board[a-1][b] = ' '
        zeilen2 = zeilen2-1 # für das nächste repeat eine zeile nach oben
        a = zeilen2
        d = 0 #resette den counter
    a = 4 # wieder nach unten in den zeilen
    for i in range (5): # gehe alle felder in der Spalte durch und wenn eines leer ist fülle es mit einer zufälligen zahl auf
        if board[a][b] == ' ': #feldauffüllen
            board[a][b] = random.choice(numbers)
        a = a-1
    b = b+1 # gehe nach spalte 2
    a = 4
    feldverschiebung(a, b)

def spielende():
    global Gameover
    if board[zeilenauswahl][spaltenauswahl] == 128:
        print ('Sieg')
        nochmal = True
        global loop
        while nochmal : # wiederhole bis 1 oder 0 eingegeben wurde
            loop = input('möchstest du noch eine Runde spielen? 1 = Ja, 0 = Nein')
            if loop == '0':
                nochmal = False
            if loop == '1':
                nochmal = False
            if loop == '0': # will der spieler nicht mehr spielen beende den code
                Gameover = True
    if loss > 0: # kommt aus der definition lost
        print ('du hast verloren')
        nochmal = True
        while nochmal :
            loop = input('möchstest du noch eine Runde spielen? 1 = Ja, 0 = Nein')
            if loop == '0':
                nochmal = False
            if loop == '1':
                nochmal = False
            if loop == '0':
                Gameover = True

def feldauffüllen():
    if leer > 1: # leer kommt aus der definition leerefelder
        board[zeilenauswahl][spaltenauswahl] = save*2 # floodfill löscht auch das ausgewählt feld also fülle es wieder auf und verdopple es
    else: # hat die eingabe nicht bewirkt dann fülle die gleiche zahl wieder ein die durch floodfill gelöscht wurde
        board[zeilenauswahl][spaltenauswahl] = save

def neuesboard():
    global loop # loop kommt aus spielende ist wird 1 gesetzt wenn noch eine runde gespielt werden will.
    if loop == '1':
        global board # ersetze das ganze board mit zufälligen zahlen
        board = [
        [random.choice(numbers),random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)],
        [random.choice(numbers),random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)],
        [random.choice(numbers),random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)],
        [random.choice(numbers),random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)],
        [random.choice(numbers),random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)]
            ]
        spielfeld()
        loop = 0

def lost(x, y): # schaut ob kein spielzug mehr möglich ist
    global loss # wenn keiner mehr möglich ist dann ist loss > 0
    if y >= len(board): # wenn ich bei reihe 6 ankomme beende die definition
        return
    old = board[x][y] # wert vom momentanen feld
    x = x-1 # gehe in den zeilen eine nach oben
    for i in range(4):
        if board[x][y] != old: # ist die zeile über mir nicht gleich ist kein spielzug möglich
            loss = loss +1
        if board[x][y] == old: # ist ein spielzug möglich wird die definition beendet
            loss = 0 # heisst es ist mindestens ein Spielzug möglich
            return
        old = board[x][y]
        x = x-1
    x = 4
    y = y+1
    lost(x, y)

Gameover = False
loop = 0
loss = 0
zeilenauswahl = 0
spaltenauswahl = 0

while not Gameover:
    zeilen = 4
    spalten = 0
    leer = 0
    lost(zeilen, spalten)
    spielende()
    neuesboard()
    loss = 0
    zeilenauswahl = input('Welche Zeile 1-5?')
    spaltenauswahl = input('Welche Spalte 1-5?')
    zeilenauswahl = überprufung(zeilenauswahl, 'Zeile')
    spaltenauswahl = überprufung(spaltenauswahl, 'Spalte')
    save = board[zeilenauswahl][spaltenauswahl]
    flood_fill(zeilenauswahl, spaltenauswahl, board[zeilenauswahl][spaltenauswahl], ' ')
    leerefelder(zeilen, spalten, leer)
    feldauffüllen()
    feldverschiebung(zeilen, spalten)
    spielfeld()