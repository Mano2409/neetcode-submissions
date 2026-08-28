# 69. Sqrt(x)
  
<br>**Problem:** https://leetcode.com/problems/sqrtx/<br>

**Difficulty:** Easy<br>
**Topics:** Math, Binary Search, Newton's Method<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-28 12:02 local time

**Runtime:** 3 ms (beats 69.2032%)
**Memory:** 19.2 MB (beats 87.7426%)


<!-- leetgit:submissionId=2122618683 codeHash=d1dde82f670bcf0cf125693fee1252c4ded88ed2f2c26b37343c73d105c31fb9 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left=1
        right=x//2
        while left<=right:
            mid=left+((right-left)//2)
            square=mid*mid
            if square==x:
                return mid
            elif square< x:
                left=mid+1
            else:
                right=mid-1
        return right
        
```
