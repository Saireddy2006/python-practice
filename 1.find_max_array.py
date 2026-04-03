# TO FIND MAX NUMBER IN ARRAY
def find_max_array(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

print(find_max_array([5, 2, 9, 6, 3]))


# TO FIND MAX INDEX IN ARRAY

# def find_max_array(arr):
#     max = arr[0]
#     max_index = 0             #assigning max index to 0
#     for i in range(1,len(arr)):
#         if arr[i] > max:
#             max = arr[i]
#             max_index = i     # max index assigend to highest value index
#     return max_index           #if you need max index uncomment it.
# print(find_max_array([5, 2, 9, 6, 3]))
