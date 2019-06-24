# Best = n*log(n)   Average = n*log(n)    Worst=n(logn)
# space = N
def merge_sort(unsorted_array):
    if len(unsorted_array) < 2:
        return unsorted_array
    midpoint = int(len(unsorted_array)/2)
    left = merge_sort(unsorted_array[:midpoint])
    right = merge_sort(unsorted_array[midpoint:])
    return merge(left, right)

def merge(a, b):
    merged = []
    a_index = 0
    b_index = 0
    while a_index < len(a) and b_index < len(b):
        # a is smaller
        if a[a_index] < b[b_index]:
            merged.append(a[a_index])
            a_index += 1
        else:
            merged.append(b[b_index])
            b_index += 1
    if a_index == len(a):
        merged = merged + b[b_index:]
    else:
     merged = merged + a[a_index:]
    return merged

print(merge_sort([2,1]))