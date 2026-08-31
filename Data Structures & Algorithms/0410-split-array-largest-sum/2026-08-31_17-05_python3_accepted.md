# 410. Split Array Largest Sum
  
<br>**Problem:** https://leetcode.com/problems/split-array-largest-sum/<br>

**Difficulty:** Hard<br>
**Topics:** Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-31 17:05 local time

**Runtime:** 3 ms (beats 71.4101%)
**Memory:** 19.4 MB (beats 46.79550000000001%)


<!-- leetgit:submissionId=2126037858 codeHash=c24693174256cfc642ef5e5c3fd40f24aab6db6f293780f69c2dfba481fc3073 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            final=self.func(nums,mid)

            if final>k:
                low=mid+1
    
            else:
                high=mid-1
        return low

    def func(self,nums,mid):
        sum=0
        counter=1
        for i in nums:
            if sum+i<=mid:
                sum+=i
            else:
                counter+=1
                sum=0
                sum+=i
        return counter


        
```
