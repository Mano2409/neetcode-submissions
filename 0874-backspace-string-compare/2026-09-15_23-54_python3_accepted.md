# 874. Backspace String Compare
  
<br>**Problem:** https://leetcode.com/problems/backspace-string-compare/<br>

**Difficulty:** Easy<br>
**Topics:** Two Pointers, String, Stack, Simulation<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-15 23:54 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.2 MB (beats 65.20870000000001%)


<!-- leetgit:submissionId=2142960645 codeHash=7c95a8933b2c3019d4757ea9bcc8318555f309044ca996360639a5d16137c34d notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
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
```
