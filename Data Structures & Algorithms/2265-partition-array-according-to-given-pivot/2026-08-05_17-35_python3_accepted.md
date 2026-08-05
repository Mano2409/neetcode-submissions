# 2265. Partition Array According to Given Pivot
  
<br>**Problem:** https://leetcode.com/problems/partition-array-according-to-given-pivot/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Two Pointers, Simulation<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-05 17:35 local time

**Runtime:** 71 ms (beats 11.09930000000001%)
**Memory:** 33.6 MB (beats 91.67769999999997%)


<!-- leetgit:submissionId=2095272889 codeHash=cd5239793dcdb3ab12ceb50647804cc189ee2b5ce08a321a07f1619ddf396d9b notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = 0
        less = []
        equal = []
        greater = []

        while left < len(nums):
            if nums[left] < pivot:
                less.append(nums[left])
                left += 1
            elif nums[left] == pivot:
                equal.append(nums[left])
                left += 1
            else:
                greater.append(nums[left])
                left += 1

        return less + equal + greater
```
