# REVERSING A STRING

# def reverse_string(str):
#     rev = ""
#     for i in range(len(str)-1, -1, -1):
#         rev = rev + str[i]
#     return rev

# print(reverse_string("hello"))

def reverse_string(str):
    rev = ""
    for i in str[::-1]:
        rev += i
    return rev
str = "banana"
print(reverse_string(str))

