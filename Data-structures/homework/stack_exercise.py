#Exercise 1
def reverse_str(s):
    reverse_string = ""
    stack = []

    for char in s:
        stack.append(char)

    while stack:
        reverse_string += stack.pop()

    return reverse_string

result = reverse_str("I am the king of my house cuh")
print(result)

#Exercise 2
def check_parentheses(s):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}

    def is_empty():
        return len(stack) == 0

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")}]":
            if is_empty() or stack.pop() != matching_brackets[char]:
                return False

    return is_empty()

print(check_parentheses("({a+b})"))
print(check_parentheses("))((a+b}{"))
