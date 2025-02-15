class Solution:
    def can_partition(self, num_str: str, target: int, index: int, current_sum: int) -> bool:
        if index == len(num_str):  
            return current_sum == target  

        for j in range(index, len(num_str)):  # Try different partitions
            part = int(num_str[index:j + 1])  # Convert substring to integer
            if current_sum + part <= target:  # Only proceed if sum doesn't exceed target
                if self.can_partition(num_str, target, j + 1, current_sum + part):
                    return True
        return False

    def punishmentNumber(self, n: int) -> int:
        punishment_sum = 0
        for i in range(1, n + 1):
            square_str = str(i * i)  # Convert square to string
            if self.can_partition(square_str, i, 0, 0):  # Check if partitioning is valid
                punishment_sum += i * i  # Add square to result
        return punishment_sum