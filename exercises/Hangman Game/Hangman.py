# Variablen
from operator import ge


gesucht = 'test'

gefunden = []
falsch_geraten = []

def show():
    print('Falsche Buchstaben:', falsch_geraten)
    for buchstabe in gesucht:
        if buchstabe in gefunden:
            print(buchstabe, end=' ')
        else:
            print('_', end=' ')
    print('')

def is_valid(inp):
    return True

def eingabe():
    buchstabe = input('Buchstabe? ')
    while not is_valid(buchstabe):
            buchstabe = input('Buchstabe? ')
    return buchstabe.lower()

def auswerten(valid_inp):
    if valid_inp in gesucht:
        gefunden.append(valid_inp)
    else:
        falsch_geraten.append(valid_inp)

def gewonnen():
    for buchstabe in gesucht:
        if buchstabe not in gefunden:
            return False
    return True

def game_over():
    size = 1
    for x in falsch_geraten:
        size+=1
    print(size)
    Versuche = 10
    if size == Versuche:
        print('FETT ALARM')
        return True
    return gewonnen()

def play():
    while not game_over():
        BUCHSTABE = eingabe() 
        auswerten(BUCHSTABE)
        show()
        print(gefunden)
        print(gesucht)
       
    if gewonnen():
        print('Du hast das Wort erraten!')
    else:
        print('Du hast verloren!')



play()