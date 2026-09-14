class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result=[]
        words.sort()
        for i in range(len(words)):
            s=words[i]
            for j in range(len(words)):
                if i==j:
                    continue
                if s in words[j]:
                    result.append(s)
                    break
        return result
                