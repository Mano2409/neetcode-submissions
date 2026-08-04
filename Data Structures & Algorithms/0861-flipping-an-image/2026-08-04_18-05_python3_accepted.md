# 861. Flipping an Image
  
<br>**Problem:** https://leetcode.com/problems/flipping-an-image/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Two Pointers, Bit Manipulation, Matrix, Simulation<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-04 18:05 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.4 MB (beats 22.757200000000005%)


<!-- leetgit:submissionId=2093967454 codeHash=dd8b75cbf749cdf1ea8fc99d6dc65898d9633726eb0d63b5224ee2d50b5da7f9 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i].reverse()
        
            first=0
            while first <len(image[i]):
                if image[i][first]==0:
                    image[i][first]=1
        
                else:
                    image[i][first]=0
                first+=1
        return image 
                
        
```
