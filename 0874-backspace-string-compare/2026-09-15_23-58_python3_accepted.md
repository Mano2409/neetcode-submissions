# 874. Backspace String Compare
  
<br>**Problem:** https://leetcode.com/problems/backspace-string-compare/<br>

**Difficulty:** Easy<br>
**Topics:** Two Pointers, String, Stack, Simulation<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-15 23:58 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.2 MB (beats 65.20870000000001%)


<!-- leetgit:submissionId=2142965851 codeHash=194d749209c586bf9fd8e8151ff776c755fbbd059f1509b4d809498f90af1607 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        string = []

        for i in range(len(s)):
            if s[i] == "#":
                if string:
                    string.pop()
            else:
                string.append(s[i])

        str_sec = []

        for i in range(len(t)):
            if t[i] == "#":
                if str_sec:
                    str_sec.pop()
            else:
                str_sec.append(t[i])

        return string == str_sec
```
