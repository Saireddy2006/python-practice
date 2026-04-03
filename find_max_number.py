# Max number in the array
def find_max_number(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i] 
    return max

#sort array to decending order
def selection_sort(arr):
    new_array = []
    for i in range(0, len(arr)):
        max = find_max_number(arr)
        max_index = arr.index(max)
        new_array.append(arr.pop(max_index))
    return new_array
print(selection_sort([3, 5, 2, 9, 6]))


#Method 2 - interviewer point of code for SELECTION SORT in DECENDING ORDER
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr
print(selection_sort([4,2,8,5,9]))


