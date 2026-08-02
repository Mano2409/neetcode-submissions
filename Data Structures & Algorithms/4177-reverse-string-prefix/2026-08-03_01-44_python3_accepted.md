# 4177. Reverse String Prefix
  
<br>**Problem:** https://leetcode.com/problems/reverse-string-prefix/<br>

**Difficulty:** Easy<br>
**Topics:** Two Pointers, String<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-03 01:44 local time

**Runtime:** 4 ms (beats 4.377100000000006%)
**Memory:** 19.3 MB (beats 15.993200000000009%)


<!-- leetgit:submissionId=2091857888 codeHash=395fb806e480b93e3b23ee87ee2154f5bbac6c26a7d0ae79c6e938e71b512689 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        left = 0
        right = k - 1
        s = list(s)
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
```
