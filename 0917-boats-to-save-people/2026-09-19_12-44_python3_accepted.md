# 917. Boats to Save People
  
<br>**Problem:** https://leetcode.com/problems/boats-to-save-people/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Two Pointers, Greedy, Sorting, Timsort<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-19 12:44 local time

**Runtime:** 47 ms (beats 88.49049999999998%)
**Memory:** 25.1 MB (beats 80.599%)


<!-- leetgit:submissionId=2146409082 codeHash=2537d44c24922ec0200bda1fca90369f3681ec93997310c60cb8d3333a47266d notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left=0
        right=len(people)-1
        count=0
        while left<=right:
            if people[left]+people[right]<=limit:
                left+=1
                right-=1
                count+=1
            else:
                right-=1
                count+=1

                
        return count



        
```
