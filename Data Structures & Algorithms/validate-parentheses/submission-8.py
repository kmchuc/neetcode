class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"]": "[", ")": "(", "}": "{"}

        stack = []

        for char in s:
            if char not in parentheses:
                stack.append(char)
            else:
                if stack:
                    last = stack.pop()
                
                    if last != parentheses[char]:
                        return False
                    else:
                        continue
                else:
                    return False
        if stack:
            return False
        else:
            return True