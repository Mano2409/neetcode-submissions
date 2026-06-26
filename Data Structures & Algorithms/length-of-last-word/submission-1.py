
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        h=s.split()
        if len(h)==0:
            return 0
        return len(h[-1])