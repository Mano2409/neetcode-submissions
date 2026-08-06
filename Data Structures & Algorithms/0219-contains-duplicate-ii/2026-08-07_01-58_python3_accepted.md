# 219. Contains Duplicate II
  
<br>**Problem:** https://leetcode.com/problems/contains-duplicate-ii/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Hash Table, Sliding Window<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-07 01:58 local time

**Runtime:** 43 ms (beats 33.32879999999998%)
**Memory:** 39.3 MB (beats 18.073799999999952%)


<!-- leetgit:submissionId=2097250998 codeHash=ab0d3d6856d1ecc06c3757bdc68fba4ae15f0983d47fe3edeb246fed77baffde notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int):
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False
        
```
