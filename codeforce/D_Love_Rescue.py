n = int(input())
word1 = list(input())
word2 = list(input())
answers = []
for index in range(n):
    first = word1[index]
    second = word2[index]
    if first != second:
        answers.append([first, second])
        for i in range(n):
            if word1[i] == first:
                word1[i] = second
            if word2[i] == first:
                word2[i] = second
print(len(answers))
for i in answers:
    print(*i)
