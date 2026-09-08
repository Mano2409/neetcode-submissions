# 2048. Build Array from Permutation
  
<br>**Problem:** https://leetcode.com/problems/build-array-from-permutation/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Simulation<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-09 00:56 local time

**Runtime:** 3 ms (beats 52.89240000000001%)
**Memory:** 19.4 MB (beats 27.266%)


<!-- leetgit:submissionId=2135580205 codeHash=b0e55360da73e1756bee289393e31a0c50394fc970421bc44b9c0c77d4c486be notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def buildArray(self, nums):
        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans
```
