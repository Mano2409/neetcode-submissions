# 240. Search a 2D Matrix II
  
<br>**Problem:** https://leetcode.com/problems/search-a-2d-matrix-ii/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search, Divide and Conquer, Matrix<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-10 01:29 local time

**Runtime:** 111 ms (beats 99.86889999999997%)
**Memory:** 25.7 MB (beats 23.359999999999992%)


<!-- leetgit:submissionId=2136817588 codeHash=fd3400e5e6c88a1b165f0473833030d89aa38e0208db0001585ea0e4fb505998 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m=len(matrix)-1
        n=len(matrix[0])-1
        row=0
        column=n
        while row<=m and column>=0:
           
            if matrix[row][column]>target:
                column-=1
            elif matrix[row][column]==target:
                return True
            else:
                row+=1
        return False 
```
