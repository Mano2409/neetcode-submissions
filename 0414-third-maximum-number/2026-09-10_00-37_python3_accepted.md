# 414. Third Maximum Number
  
<br>**Problem:** https://leetcode.com/problems/third-maximum-number/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Sorting<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-10 00:37 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 20.7 MB (beats 8.142799999999973%)


<!-- leetgit:submissionId=2136779617 codeHash=e6566f2cbc41b149e12b3dbfbce075542e3701cabdec0cfd42f85bb88f47b4ef notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def thirdMax(self, nums: List[int]) -> int: 
        nums=list(set(nums))
        nums.sort(reverse=True)
        if len(nums)<3:
            return nums[0]
        count=0
        for i in nums:
            count+=1
            if count==3:
                return i
    
            

```
