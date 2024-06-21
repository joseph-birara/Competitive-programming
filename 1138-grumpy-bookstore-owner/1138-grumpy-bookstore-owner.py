

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_satisfied = 0
        n = len(grumpy)

        # Calculate the number of customers satisfied when the owner is not grumpy
        for i in range(n):
            if grumpy[i] == 0:
                total_satisfied += customers[i]

        # Use a sliding window to find the maximum number of customers that can be satisfied
        # during 'minutes' minutes of the grumpy owner's happiness
        max_additional_satisfied = 0
        current_additional_satisfied = 0

        for i in range(n):
            # Add customers of the current window if the owner is grumpy
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
            
            # Remove customers from the left side of the window if it exceeds the given minutes
            if i >= minutes and grumpy[i - minutes] == 1:
                current_additional_satisfied -= customers[i - minutes]
            
            # Update the maximum additional satisfied customers
            max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)

        # The result is the sum of always satisfied customers and the maximum additional satisfied customers
        return total_satisfied + max_additional_satisfied
