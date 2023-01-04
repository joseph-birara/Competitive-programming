

number_of_testCases = int(input())
for test in range(number_of_testCases):

    array_length = int(input())
    array_elements = list(map(int,input().split()))
    stringS = input()
    count = {}
    flag = True
    for index in range(array_length):
        if array_elements[index] not in count.keys():
            count[array_elements[index]] = stringS[index]
        else:
            if count[array_elements[index]] != stringS[index]:
                print("No")
                flag = False
                break
            else:
                continue
    if flag:
        print("YES")
    



