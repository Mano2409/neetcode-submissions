# 74. Search a 2D Matrix
  
<br>**Problem:** https://leetcode.com/problems/search-a-2d-matrix/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search, Matrix<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-09 01:52 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.7 MB (beats 13.828600000000005%)


<!-- leetgit:submissionId=2135616090 codeHash=ac91578e152161957be86f0a3ac1d1717e7b66f9715c1f4d6e15bd6717585d45 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=(n*m)-1
        while low<=high:
            mid=(low+high)//2
            row=mid//m
            column=mid%m
            final=matrix[row][column]
            if final==target:
                return True
            elif final>target:
                high=mid-1
            else:
                low=mid+1
        return False 


        

```
