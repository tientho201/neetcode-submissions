
class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        for char in s:
            if char in pairs.values():
                myStack.append(char)
            else:
                if not myStack or myStack[-1] != pairs[char]:
                    return False
                myStack.pop()
        return not myStack

