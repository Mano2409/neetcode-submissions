# 1524. String Matching in an Array
  
<br>**Problem:** https://leetcode.com/problems/string-matching-in-an-array/<br>

**Difficulty:** Easy<br>
**Topics:** Array, String, String Matching<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-14 20:28 local time

**Runtime:** 2 ms (beats 73.57209999999999%)
**Memory:** 19.5 MB (beats 24.104600000000005%)


<!-- leetgit:submissionId=2141679337 codeHash=a6cdae02ef4098fdb25efcaaf5af031d5efcdaa45e446048d9616c935e2eb83f notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        words.sort()

        for i in range(len(words)):
            sample = words[i]

            for j in range(len(words)):
                if i == j:
                    continue

                if sample in words[j]:
                    result.append(sample)
                    break

        return result
```
