class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")" : "(", "]" : "[", "}" : "{"}
        for char in s:
            if char in brackets:
                if stack:
                    element = stack.pop()
                    if element != brackets[char]:
                        return False
                else:
                    return False
            else:
                stack.append(char)

        return not stack

if __name__ == "__main__":
    s = "()[]}"
    obj_name = Solution()
    result = obj_name.isValid(s)
    print(result)
