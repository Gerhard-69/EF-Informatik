import sys
sys.setrecursionlimit(1000)

def  ack(m, n):
    if m == 0:
        anw = n+1
    else:
        if n == 0:
            anw = ack(m-1, 1)
        else:
            anw = ack(m-1,ack(m,n-1))
    return anw

m = 4
n = 1
print (m, n, ack(m,n))