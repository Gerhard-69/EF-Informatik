board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]
#Zahlen oben
x = 0
for i in board:
    x = x+1
    print ('', x, end='')
print (' ')

#Zahlen seite


for zeile in board:
    for zelle in zeile:
        print(' -', end='')
    print(' ',)
    print (' ', end='')
    for zelle in zeile:
        print(f'|{zelle}', end='')
    print('|')
    print (' ', end='')

for zelle in board[0]:
    print(' -', end='')
print(' ')