import random
random.seed(2)
numbers = [1, 2, 4, 8] # bestimmt die zahlen die zufällig ausgewählt werden

board = []
Row = 5

def field_fill():
    for i in range(Row):
        board.append([])
        for j in range(Row):
            randomint = random.choice(numbers)
            board[i].append(randomint) #For loop um das Feld am Anfang aufzufüllen
field_fill()

def spielfeld(): # erstelle das Spielfeld
    #Zahlen oben = x
    x = 0
    y = 0 
    print ('  ', end='')
    for i in board: # Beschriftung reihen
        x = x+1
        print ('  ', x, end='')
    print (' ') # neue zeile
    print ('   ', end='') # abstand und auf gleicher zeile bleiben
    for zeile in board: # wiederhole für die anzahl zeilen
        for zelle in zeile: # widerhole für die anzahl reihen
            print('----', end='')
        print(' ',) # neues zeile
        print (' ', end='') #abstand und auf gleicher zeile bleiben
        y = y+1 #Zahlen seite
        print (y, end='')
        for zelle in zeile: # wiederhole für anzahl reihen
            if zelle > 10: # wenn zahl zweistellig kleinerer abstand
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
    try: # wenn error gehe in except
        zahl = int(raw) # ändere zahl zu einen integrer
        zahl = zahl -1 # verkleinere Zahl um 1 weil in matrix erste stelle gleich 0 ist
        if zahl > 5: # ist die zahl zu gross mache künstlichen fehler
            raise
        if zahl <= -1:# ist die zahl zu klein mache künstlichen fehler
            raise
        return zahl
    except: # wenn error oder raise
        print ('Fehlerhafte Eingabe')
        zeilenauswahl = input(f'Welche {richtung} 1-5?') # frage erneut nach der falschen eingabe
        zeilenauswahl = überprufung(zeilenauswahl, richtung) #wiederhole überprüfung
        return zeilenauswahl # gib die erneute überprüfung zurück

def flood_fill(x, y, old, new):
    if x >= len(board) or x == -1: # ist zeile aus dem feld dann beende
        return
    if y >= len(board) or y == -1: # ist reihe aus dem feld dann beende
        return
    if board[x][y] != old: # gleiche zahl wie altes feld dann beende
        return
    board[x][y] = new # wenn kein return dann leere das feld
    flood_fill(x+1, y, old, new) # gehe in den zeilen eins nach unten
    flood_fill(x-1, y, old, new) # gehe in den zeilen eins nach oben
    flood_fill(x, y+1, old, new) # gehe in den reihen eins nach rechts
    flood_fill(x, y-1, old, new) # gehe in den reihen eins nach links

def leerefelder(c, d, e):
    global leer # beziehe und verändere dich auf die globale variable
    if d >= len(board): # wenn spalten grösser als das board spalten hat beende
        return
    for i in range(5):
        if (board[c][d]) == ' ': # ist das feld leer dann
            e = e+1 # erhöre denn leerefelder zähler
            leer = e # setze die variable  mit dem zähler gleich
        c = c-1 # gehe eine zeile nach oben
    d = d+1 # gehe in die nächste reihe
    c = 4 # gehe wieder nach zeile 5
    leerefelder(c, d, e)

def feldverschiebung(a, b):
    d = 0 # d beschreibt ob ein grösserer Sprung schon gemacht wurde.
    zeilen2 = 4 # merkt sich Zeile in der ich mich befinde
    if b >= len(board): # wenn spalten grösser als das board spalten hat beende
        return
    for i in range (4):
        if board[a][b] == ' ':
            if a-2 > -1: # wenn a < 0 wäre würde ich wieder unten im Feld landen. mit diesem if verhindere ich es
                if board[a-1][b] == ' ': # ist das feld über dem leeren feld auch leer? (zwei hintereinander)
                    board[zeilen2][b] = board[a-2][b]
                    board[a-2][b] = ' '
                    if board[a][b] == ' ': # wenn das feld immer noch leer ist
                        d = d + 1
                    if d == 1: # wenn das feld nicht mehr leer ist würden die nächsten zeilen code alles zerstören
                        if a-3 > -1:
                            if board[a-2][b] == ' ':
                                board[zeilen2][b] = board[a-3][b]
                                board[a-3][b] = ' '
                                if board[a][b] == ' ': # wenn das feld immer noch leer ist
                                    d = d + 1
                                if d == 2: # wenn das feld nicht mehr leer ist würden die nächsten zeilen code alles zerstören
                                    if a-4 > -1:
                                        if board[a-3][b] == ' ':
                                            board[zeilen2][b] = board[a-4][b]
                                            board[a-4][b] = ' '
            if board[a][b] == ' ': # ist das feld immernoch leer
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
        field_fill()
        spielfeld()
        loop = 0

def lost(x, y): # schaut ob kein spielzug mehr möglich ist
    global loss # wenn keiner mehr möglich ist dann ist loss > 0
    if y >= len(board): # wenn ich bei reihe 6 ankomme beende die definition
        return
    for i in range(5):
        old = board[x][y] # wert vom momentanen feld
        if x > 0:
            if board[x-1][y] != old: # ist das feld über mir nicht gleich ist kein spielzug möglich
                loss = loss + 1
        if y < 4: # wenn y = 4 gibt es keine weitere reihe
            if board[x][y+1] != old: # ist das feld in der nächsten reihe nicht gleich ist kein spielzug möglich
                loss = loss + 1
        if x > 0:
            if board[x-1][y] == old: # ist ein spielzug möglich wird die definition beendet
                loss = 0 # heisst es ist mindestens ein Spielzug möglich
                return
        if y < 4:
            if board[x][y+1] == old: # ist ein spielzug möglich wird die definition beendet
                loss = 0 # heisst es ist mindestens ein Spielzug möglich
                return
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
    lost(zeilen, spalten) # überprüfe ob kein Spielzug mehr möglich ist
    spielende() # überprüft ob das spiel zu ende ist
    neuesboard() # erstellt wenn das spiel nochmal gespielt wird ein neues spielfeld
    loss = 0
    zeilenauswahl = input('Welche Zeile 1-5?')
    spaltenauswahl = input('Welche Spalte 1-5?')
    zeilenauswahl = überprufung(zeilenauswahl, 'Zeile')
    spaltenauswahl = überprufung(spaltenauswahl, 'Spalte')
    save = board[zeilenauswahl][spaltenauswahl]
    flood_fill(zeilenauswahl, spaltenauswahl, board[zeilenauswahl][spaltenauswahl], ' ') # leere die felder die gleich und anliegend zu dem wausgewählten feld sind 
    leerefelder(zeilen, spalten, leer) # zähle die leeren felder
    feldauffüllen() # fülle das ausgewählte feld das durch floodfill geleert wurde wieder auf
    feldverschiebung(zeilen, spalten) # schiebe leere felder nach oben und fülle diese mit zufälligen zahlen
    spielfeld()

