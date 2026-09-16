class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        left = len(s) - 1
        left2 = len(t) - 1
        
        while left >= 0 or left2 >= 0:
            # skip logic for s
            skip = 0
            while left >= 0:
                if s[left] == '#':
                    skip += 1
                    left -= 1
                elif skip > 0:
                    skip -= 1
                    left -= 1
                else:
                    break
            
            # skip logic for t
            skip2 = 0
            while left2 >= 0:
                if t[left2] == '#':
                    skip2 += 1
                    left2 -= 1
                elif skip2 > 0:
                    skip2 -= 1
                    left2 -= 1
                else:
                    break
            
            # now compare landed positions
            if left >= 0 and left2 >= 0:
                if s[left] != t[left2]:
                    return False
            elif left >= 0 or left2 >= 0:
                # one string still has a real char, other ran out
                return False
            
            left -= 1
            left2 -= 1
        
        return True