class Solution:
    def checkString(self, s: str) -> bool:
        idx = s.find('b')
        if idx == -1: return True
        while idx < len(s):
            if s[idx] == 'a':
                return False
            idx += 1
        return True