def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    
    return prefix
strs = ["flower","flow","flight","flourish"]
result = longestCommonPrefix(strs)
print(result)  # Output: "fl"