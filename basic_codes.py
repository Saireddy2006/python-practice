# FIND MAXIMUM NUMBER IN A LIST

# nums = [3, 5, 7, 2, 8]
# def basic_codes(nums):
#     max_num = 0
#     for i in nums:
#         if i > max_num:
#             max_num = i
#     return max_num
# result = basic_codes(nums)
# print(result)  # Output: 8



# COUNT THE FREQUENCY OF CHAR IN STRING

# def basic_codes(str):
#     count = 0
#     for ch in str:
#         if ch == "a":
#             count += 1
#     return count
# str = "banana"
# result = basic_codes(str)
# print(result)



# SUM OF ALL ELEMENTS

# def basic_codes(nums):
#     sum = 0
#     for i in nums:
#         sum = sum + i
#     return sum
# nums = [1,2,3,4]
# result = basic_codes(nums)
# print(result)



# CHECK IF NUMBER EXISTS IN LIST

# def basic_codes(nums):
#     for i in nums:
#         if i == 20:
#             return True
#     return False
# nums = [12,20,30]
# result = basic_codes(nums)
# print(result)



# PRINT ALL EVEN NUMBERS IN LIST

# def basic_codes(nums):
#     new_list = []
#     for i in nums:
#         if i%2 == 0:
#             new_list.append(i)
#     return new_list
# nums = [1,2,3,5,6,7,9,10,12]
# result = basic_codes(nums)
# print(result)
        


# REVERSE A STRING 

# def basic_codes(str):
#     rev = ""
#     for i in str[::-1]:
#         rev += i
#     return rev
# str = "sai tej"
# print(basic_codes(str))



# FIND THE MININUM ELEMENT

# nums = [8, 3, 5, 1, 9]
# def basic_codes(nums):
#     min = nums[0]
#     for i in nums[1:]:
#         if i < min:
#             min = i
#     return min
# print(basic_codes(nums))



# COUNT VOWELS IN STRING

# s = "programming"
# def basic_codes(s):
#     count = 0
#     for i in s:
#         if i  in "aeiou":
#             count += 1
#     return count
# print(basic_codes(s))



# REMOVE DUPLICATE NUMBERS

# nums = [1,2,3,4,5,2,4,5,6]
# def basic_codes(nums):
#     new_list = []
#     for i in nums:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
# print(basic_codes(nums))



# RETURN FIRST NON-REPEATING CHARACTER:

# s = "aabbcdd"
# def basic_codes(s):
#     result = " "
#     for i in s:
#         if s.count(i) == 1:
#             result += i
#     return result
# print(basic_codes(s))



# CHECK IF STRING IS PALINDROME:

# s = "racecar"
# def basic_codes(s):
#     rev = ""
#     for i in s[::-1]:
#         rev += i
#     if s == rev:
#         return True
#     return False
# print(basic_codes(s))



# EASIEST WAY OF SOLVING ABOVE PROBLEM

# def basic_codes(s):
#     return s == s[::-1]
# print(basic_codes(s))



# FIND COMMON ELEMENTS IN TWO LISTS:

# a = [1,2,3]
# b = [2,3,4]
# def basic_codes(a,b):
#     new_list = []
#     for i in a:
#         if i in b:
#             new_list.append(i)
#     return new_list
# print(basic_codes(a,b))
    


# FIND COMMON ELEMENTS IN TWO STRINGS:

# s = "hello"
# r = "apple"
# def basic_codes(s,r):
#     res = ""
#     for i in s:
#         if i in r:
#             res += i
#     return res
# print(basic_codes(s,r))



# COUNT FREQUENCY OF EACH CHARACTER:

# s = "aabccc"
# def basic_codes(s):
#     freq = {}
#     for i in s:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1
#     return freq
# print(basic_codes(s))

