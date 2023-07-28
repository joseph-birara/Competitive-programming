def check_substrings(s):

    if 'AB' in s and 'BA' in s[s.index('AB')+2:]:
        return True

    if 'BA' in s and 'AB' in s[s.index('BA')+2:]:
        return True

    return False


s = input().strip()


if check_substrings(s):
    print("YES")
else:
    print("NO")
