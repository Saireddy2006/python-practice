
def String_to_integer(s: str) -> int:
    int_max = 2**31
    int_min = -1 * int_max

    i = 0
    n = len(s)
    sign = 1
    result = 0

    while i < n and s[i] == " ":
        i += 1
    if i < n and (s[i] == '-' or s[i] == '+'):
        if s[i] == '-':
            sign = -1
        i += 1
    while i < n and s[i].isdigit():
        digit = int(s[i])

        if result > (int_max - digit) // 10:
            if sign == 1:
                return int_max
            else:
                return int_min

        result = result * 10 + digit
        i += 1

    return sign * result


print(String_to_integer("42"))           # 42
print(String_to_integer("   -042"))      # -42
print(String_to_integer("1337c0d3"))     # 1337
print(String_to_integer("0-1"))          # 0
print(String_to_integer("words and 987")) # 987