# 2463. Minimum Recolors to Get K Consecutive Black Blocks
  
<br>**Problem:** https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/<br>

**Difficulty:** Easy<br>
**Topics:** String, Sliding Window<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-06 17:47 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.3 MB (beats 59.83609999999999%)


<!-- leetgit:submissionId=2096639002 codeHash=37d42fb01a6014ca1f45a4602cc4b12d38ead485a7004fa8a6503cbdc749b64b notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=0
        for i in range(k):
            if blocks[i]=="W":
                count+=1
        res=count
        pointer=k
        while pointer<len(blocks):
            if blocks[pointer-k]=="W":
                count-=1
            if blocks[pointer]=="W":
                count+=1
            res=min(res,count)
            pointer+=1
        return res 
        
```
