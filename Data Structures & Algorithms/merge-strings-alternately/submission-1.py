class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=0
        right=0
        s=list(word1)
        k=list(word2)
        mai=[]
        while left<len(word1) and right<len(word2):
            mai.append(s[left])
            mai.append(k[right])
            left+=1
            right+=1
        while right<len(word2):
            mai.append(k[right])
            right+=1
        while left<len(word1):
            mai.append(s[left])
            left+=1
        return "".join(mai)       