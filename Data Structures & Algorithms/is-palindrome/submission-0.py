import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r"[^a-z0-9]", "", s.lower())
        for i in range(0, len(result) // 2 ):
            if result[i] != result[-i - 1 ]:
                return False
     
        return True