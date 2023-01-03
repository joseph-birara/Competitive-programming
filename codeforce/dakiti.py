import re


def num_sort(test_string):
    return list(map(int, re.findall(r'\d+', test_string)))[0]
testCase = int(input())
for i in range(testCase):
    phrase = list(input().split())
    phrase.sort(key=num_sort)
    res = ''
    d = len(phrase)
    for word in phrase:
        d +=1
        res += ''.join([i for i in word if not i.isdigit()])
        
        if d>0:
            res+=" "
    
    print(res)

    