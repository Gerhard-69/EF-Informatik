def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a

to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print('Unsortiert:', to_sort)
print('Sortiert:  ', insertion_sort(to_sort))