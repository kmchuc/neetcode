import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        reverse_stripped_s = stripped_s[::-1]

        if stripped_s == reverse_stripped_s:
            return True
        else:
            return False