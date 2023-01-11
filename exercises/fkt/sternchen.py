'''
#Version 1
länge = input("Wie lang")
breit = input("Wie breit")
länge2 = int(länge)
breit2 = int(breit)
breit3 = breit2 - 2
def reihe():
    for i in range(länge2):
        print ("*", end="")
def breite():
    for i in range (breit2):
        print ("")
        print ("*", end="")
        for i in range (breit3):
            print (' ', end="")
        print("*", end="")
    print ("")
reihe()
breite()
reihe()

#Version 2
länge = int (input("Wie lang"))
breit = int (input("Wie breit"))
breit2 = breit - 2
def reihe():
    for i in range(länge):
        print ("*", end="",)
    print ("")
def breite():
    for i in range (breit):
        print ("" + "*" + ' ' * breit2 + "*")
reihe()
breite()
reihe()
'''
#Finale Version
länge = int (input("Wie lang"))
breit = int (input("Wie breit"))
breit2 = breit - 2
def marcus():
    for i in range(länge):
        print ("*" * länge)
    for i in range (breit):
        print ("" + "*" + ' ' * breit2 + "*")
    for i in range(länge):
        print ("*", end="",)
marcus()