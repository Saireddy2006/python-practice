def longest_palindrome_substring(s):
    longest_sub = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1]:
                if len(sub)>len(longest_sub):
                    longest_sub = sub
    return longest_sub

s = "babcd"
print(longest_palindrome_substring(s))
