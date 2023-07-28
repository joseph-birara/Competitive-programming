testCAse = int(input())


def operation(n, num1, num2):
    index = len(number)-1
    while index > -1 and number[index] != n:
        index -= 1

    index -= 1
    if index >= 0:
        while index >= 0 and number[index] != num1 and number[index] != num2:
            index -= 1
    if index > -1:
        return (len(number) - index) - 1
    else:
        return 50


for i in range(testCAse):
    number = input()
    min_5 = operation("5", "2", "7")
    min_0 = operation("0", "0", "5")

    print(min(min_0, min_5)-1)
