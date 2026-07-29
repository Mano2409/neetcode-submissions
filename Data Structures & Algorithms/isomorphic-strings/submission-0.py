class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s=[i for i in s]
        k=[j for j in t]

        if len(s)!=len(t):
            return False 
        ss={}
        con=0
        for l in range(len(s)):
            if s[l] not in ss and k[l] not in ss.values():
                ss[s[l]]=k[l]
                con+=1
            elif s[l] in ss:
                if ss[s[l]]==k[l]:
                    con+=1
        return con==len(k)

        