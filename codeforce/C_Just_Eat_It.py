
num_test_cases = int(input())


for _ in range(num_test_cases):    
    n = int(input())   
   
    s = list(map(int, input().split()))
   
    total_sum = sum(s)
    
   
    left_sum = 0
    right_sum = 0
    result = 'YES'
    
    # Iterate through the list, checking possible partitions
    for i in range(len(s) - 1):
        left_sum += s[i]  
        right_sum += s[-i-1]  
        
        # If either partition sum is greater than or equal to the total sum, update result to 'NO'
        if left_sum >= total_sum or right_sum >= total_sum:
            result = 'NO'
            break  # No need to continue checking
        
    
    print(result)
