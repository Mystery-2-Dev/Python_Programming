def insertion_sort(ls):
    for i in range(1, len(ls)):
        temp = ls[i]
        j = i - 1
        while (j >= 0 and temp < ls[j]):
            ls[j + 1] = ls[j]
            j = j - 1
        ls[j + 1] = temp


ls = input('Enter the list of numbers: ').split()
ls = [int(x) for x in ls]
insertion_sort(ls)
print('Sorted list: ', end='')
print(ls)
