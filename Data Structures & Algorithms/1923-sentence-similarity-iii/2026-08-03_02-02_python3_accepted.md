# 1923. Sentence Similarity III
  
<br>**Problem:** https://leetcode.com/problems/sentence-similarity-iii/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Two Pointers, String<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-03 02:02 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.3 MB (beats 65.12610000000001%)


<!-- leetgit:submissionId=2091867310 codeHash=0b1c26a5a1025f34561bd97a2123552d11d1681fc284f6f7bc8c7ae74e0f6124 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str):

        sent1 = sentence2.split()
        sent2 = sentence1.split()

        s1 = list(sent1)
        s2 = list(sent2)

        if len(s1) > len(s2):
            s1, s2 = s2, s1

        left1 = 0
        left2 = 0
        right1 = len(s1) - 1
        right2 = len(s2) - 1

        while left1 <= right1:

            if s1[left1] == s2[left2]:
                left1 += 1
                left2 += 1

            elif s1[right1] == s2[right2]:
                right1 -= 1
                right2 -= 1

            else:
                return False

        return True
```
