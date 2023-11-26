class Solution:
    def countOfAtoms(self, formula: str) -> str:
       
        stack = [{}]
        i = 0

        while i < len(formula):
            if formula[i] == '(':
                stack.append({})
                i += 1
            elif formula[i] == ')':
                current_counts = stack.pop()
                i += 1

                # Get the count of the element following the ')'
                j = i
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                count = int(formula[i:j]) if i < j else 1
                i = j

                # Update counts of elements within parentheses
                for element, element_count in current_counts.items():
                    stack[-1][element] = stack[-1].get(element, 0) + element_count * count
            else:
                # Parse the element and its count
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                element = formula[i:j]
                i = j
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                count = int(formula[i:j]) if i < j else 1
                i = j

                # Update counts outside parentheses
                stack[-1][element] = stack[-1].get(element, 0) + count

        result = ""
        for element, count in sorted(stack[-1].items()):
            result += element
            if count > 1:
                result += str(count)

        return result



        