class NumberContainers:

    def __init__(self):
        self.value_map = {}
        self.index_map = {}

    def change(self, index: int, number: int) -> None:
        prev_number = self.index_map.get(index, None)
        if prev_number is not None:
            if prev_number != number:
                self.value_map[prev_number][1].discard(index)
                if not self.value_map[prev_number][1]:
                    self.value_map[prev_number][0] = float('inf')
                else:
                    self.value_map[prev_number][0] = min(self.value_map[prev_number][1])

        self.index_map[index] = number
        if number in self.value_map:
            self.value_map[number][0] = min(self.value_map[number][0], index)
            self.value_map[number][1].add(index)
        else:
            self.value_map[number] = [index, {index}]

    def find(self, number: int) -> int:
        if number not in self.value_map or not self.value_map[number][1]:
            return -1
        return self.value_map[number][0]



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)