class Solution:
    def firstUniqChar(self, s: str) -> int:
        ss={}
        for i in s:
            if i not in ss:
                ss[i]=1
            else:
                ss[i]+=1
        for j in ss:
            if ss[j]==1:
                return s.index(j)
        return -1
        