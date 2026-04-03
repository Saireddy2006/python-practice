# brute force solution

# def length_of_longest_substring(s):
#     max_length = 0

#     for i in range(len(s)):
#         seen = set()

#         for j in range(i, len(s)):
#             if s[j] in seen:
#                 break
#             seen.add(s[j])
#             max_length = max(max_length, j - i + 1)

#     return max_length

# s = "abcabcbb"
# print(length_of_longest_substring(s))

# SLIDING WINDOW SOLUTION

def length_of_longest_substring(s):
    seen = set()          # stores characters currently in the window
    left = 0              # left pointer of window
    max_length = 0        # stores longest valid substring length

    for right in range(len(s)):   # right pointer expands window
        # If current character is already in window,
        # shrink window from left until duplicate is removed
        while s[right] in seen:   # we are using while instead of IF because while keeps removing until it is sure the duplicate is gone but if only removes one char.
            seen.remove(s[left])
            left += 1

        # Add current character to window
        seen.add(s[right])

        # Update max length of valid window
        max_length = max(max_length, right - left + 1)

    return seen


# Example input and output
s = "pwwkew"
print(length_of_longest_substring(s))   # 3