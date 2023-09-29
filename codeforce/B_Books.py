def max_books_read(n, t, books):
    left = 0  
    right = 0  
    total_time = 0  
    max_books = 0  
 
    while right < n:
        total_time += books[right]        
        while total_time > t:
            total_time -= books[left]
            left += 1        
        max_books = max(max_books, right - left + 1)
 
        right += 1  
    return max_books
 
# Read input
n, t = map(int, input().split())
books = list(map(int, input().split()))
 
print(max_books_read(n, t, books))