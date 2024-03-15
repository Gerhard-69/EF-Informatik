from timeit import timeit
from copy import deepcopy

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a

to_sort = list(range(20000))
to_sort.sort(reverse= True)

execution_time = timeit(lambda: insertion_sort(deepcopy(to_sort)), number=1)
print('Zeit für 1x Sortieren:', execution_time / 1)