from timeit import timeit
from copy import deepcopy

def selection_sort(a):
    for j in range(len(a) - 1):
        key = a[j]
        index = j
        for i in range(j + 1, len(a)):
            if a[i] < a[index]:
                index = i
        a[j] = a[index]
        a[index] = key
    return a

to_sort = list(range(10000))
to_sort.sort(reverse= True)

execution_time = timeit(lambda: selection_sort(deepcopy(to_sort)), number=5)
print('Zeit für 1x Sortieren:', execution_time / 5)