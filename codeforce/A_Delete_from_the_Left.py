s = input()
t = input()

s_len = len(s)
t_len = len(t)

while t_len > 0 and s_len > 0 and s[s_len-1] == t[t_len-1]:

    t_len -= 1
    s_len -= 1
print(s_len + t_len)
