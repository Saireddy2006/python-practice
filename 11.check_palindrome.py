def isPalindrome(x):
    # For integers, negatives are not palindromes by common convention
    if isinstance(x, int):
        if x < 0:
            return False
        s = str(x)
    else:
        s = str(x)
    return s == s[::-1]

print(isPalindrome(-121))        # Output: False
print(isPalindrome("racecar"))  # Output: True
print(isPalindrome("121"))    # Output: False