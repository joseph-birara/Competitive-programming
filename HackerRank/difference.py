# Enter your code here. Read input from STDIN. Print output to STDOUT
len_english = int(input())
english_rol = set(list(input().split()))
len_french = int(input())
french_rol = set(list(input().split()))
print(len(english_rol.difference(french_rol)))
