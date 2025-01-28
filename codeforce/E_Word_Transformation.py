
# Daisy loves playing games with words. Recently, she has been playing the following Deletive Editing word game with Daniel.

# Daisy picks a word, for example, "DETERMINED". On each game turn, Daniel calls out a letter, for example, 'E', and Daisy removes the first occurrence of this letter from the word, getting "DTERMINED". On the next turn, Daniel calls out a letter again, for example, 'D', and Daisy removes its first occurrence, getting "TERMINED". They continue with 'I', getting "TERMNED", with 'N', getting "TERMED", and with 'D', getting "TERME". Now, if Daniel calls out the letter 'E', Daisy gets "TRME", but there is no way she can get the word "TERM" if they start playing with the word "DETERMINED".

# Daisy is curious if she can get the final word of her choice, starting from the given initial word, by playing this game for zero or more turns. Your task it help her to figure this out.

# Input
# The first line of the input contains an integer n
#  — the number of test cases (1≤n≤10000
# ). The following n
#  lines contain test cases.

# Each test case consists of two words s
#  and t
#  separated by a space. Each word consists of at least one and at most 30 uppercase English letters; s
#  is the Daisy's initial word for the game; t
#  is the final word that Daisy would like to get at the end of the game.

# Output
# Output n
#  lines to the output — a single line for each test case. Output "YES" if it is possible for Daisy to get from the initial word s
#  to the final word t
#  by playing the Deletive Editing game. Output "NO" otherwise.

from collections import defaultdict, Counter

def find_last(arr, k,mth):
    count = 0
    for i in range(len(arr)-1, -1, -1): 
        if arr[i] == k:
            count += 1
            if count == mth :
                return i
    return -1

n = int(input())

for i in range(n):
    s, t = input().split()
    cnt = defaultdict(int)
    if len(t)> len(s):
        print("NO")
        continue
    if len(t)== len(s) and s != t :
        print("NO")
        continue


    
    for j in range(len(t)-1,-1, -1):
        cnt[t[j]] += 1
        flag = False
        has_printed = False
        index = find_last(s,t[j],cnt[t[j]])
        if index == -1:
            print("NO")
            has_printed = True
            break
        for k in range(j-1,-1, -1):
            new_cnt = Counter(s[index+1:])[t[k]]
            if  new_cnt > cnt[t[k]]:
                print("NO")
                has_printed = True
                flag = True
                break
        if flag:
            break
    if not has_printed:
        print("YES")
