number_of_testCases = int(input())
for testCase in range(number_of_testCases):
     t_shirt_a , t_shirt_b = input().split()
     if t_shirt_a[-1] > t_shirt_b[-1]:
        print("<")
     elif t_shirt_a[-1] < t_shirt_b[-1]:
        print(">")
     else:
        if t_shirt_a[-1]== "S":
            if len(t_shirt_a) >len(t_shirt_b):
                print("<")
            elif len(t_shirt_a) <len(t_shirt_b):
                print(">")
            else:
                print("=")
        if t_shirt_a[-1]== "L":
            if len(t_shirt_a) >len(t_shirt_b):
                print(">")
            elif len(t_shirt_a) <len(t_shirt_b):
                print("<")
            else:
                print("=")
        else:
            if t_shirt_a[-1]== "M":
                print("=")
        




    