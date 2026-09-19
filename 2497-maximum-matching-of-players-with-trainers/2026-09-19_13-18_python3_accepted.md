# 2497. Maximum Matching of Players With Trainers
  
<br>**Problem:** https://leetcode.com/problems/maximum-matching-of-players-with-trainers/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Two Pointers, Greedy, Sorting<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-19 13:18 local time

**Runtime:** 89 ms (beats 18.5495%)
**Memory:** 34.5 MB (beats 72.52440000000001%)


<!-- leetgit:submissionId=2146432240 codeHash=9aaa7319e77823fe5729429eb740c7dc9e058cac40c6e63671a064a048d328c1 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        left=0
        left1=0
        count=0
        while left<=len(players)-1 and left1<=len(trainers )-1:
            if players[left]<=trainers[left1]:
                count+=1
                left+=1
                left1+=1
            else:
                left1+=1
              
        return count 
                

        
```
