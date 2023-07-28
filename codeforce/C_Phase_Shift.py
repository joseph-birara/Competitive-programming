def get_prototype_string(t):
    s = ""
    for i in range(len(t) - 1, -1, -1):
        ascii_code = ord(t[i])
        ascii_code -= 1
        if ascii_code < 97:
            ascii_code += 26
        s += chr(ascii_code)
    return s[::-1]


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the length of the string t
    n = int(input())

    # Read the string t
    t_string = input()

    # Get the lexicographically smallest string s
    s_string = get_prototype_string(t_string)

    # Print the string s
    print(s_string)
