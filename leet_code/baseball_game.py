from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for value in operations:
            # print(f"Stack : {stack}")
            # print(f"Value : {value}")
            if value == "C":
                if stack:
                    stack.pop()
            elif value == "D":
                if stack:
                    stack.append(2*(stack[-1]))
            elif value == "+":
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(value))

        return sum(stack)

if __name__ == "__main__":
    ops = ["5", "2", "C", "D", "+"]
    obj_name = Solution()
    result = obj_name.calPoints(ops)
    print(result)