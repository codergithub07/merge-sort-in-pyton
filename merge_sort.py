# Python code for merge sort of Time Complexity: n log(n)

def merge(l, r):

    l_size = len(l)
    r_size = len(r)
    i = 0
    j = 0
    a = []

    while i < l_size and j < r_size:
        if(l[i] < r[j]):
            a.append(l[i])
            i += 1
        else:
            a.append(r[j])
            j += 1
    
    while i < l_size:
        a.append(l[i])
        i += 1
    while j < r_size:
        a.append(r[j])
        j += 1

    return a

def mergeSort(array):
    size = len(array)
    if size == 1:
        return array
    left_part = array[0:size // 2]
    right_part = array[size // 2:size]

    left_part = mergeSort(left_part)
    right_part = mergeSort(right_part)
    return merge(left_part, right_part)

a = [6, 3, 7, 4, 1, 657, 34, 23, 56, 75, 234, 67]
print(mergeSort(a))