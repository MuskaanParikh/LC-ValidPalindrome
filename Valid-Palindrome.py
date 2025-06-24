import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        return s[::-1] == s
        