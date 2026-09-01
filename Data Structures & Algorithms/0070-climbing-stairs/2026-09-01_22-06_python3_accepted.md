# 70. Climbing Stairs
  
<br>**Problem:** https://leetcode.com/problems/climbing-stairs/<br>

**Difficulty:** Easy<br>
**Topics:** Math, Dynamic Programming, Memoization<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-01 22:06 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.1 MB (beats 87.06839999999998%)


<!-- leetgit:submissionId=2127473263 codeHash=7c4717f17b2bc3dea681aae20ff368d07eb85278243f16eaa00bd7c56d0898b2 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
```
