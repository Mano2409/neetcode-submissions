class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s1=list(s)
        t2=list(t)
        left1=0
        left2=0
        for _ in range(len(s)):
            if  left2<len(t) and s1[left1]==t2[left2]:
                left1+=1
                left2+=1
            else:
                left1+=1
        return len(t2) - left2


