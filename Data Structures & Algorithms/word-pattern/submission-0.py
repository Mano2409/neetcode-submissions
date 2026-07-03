class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        coun=0
        ss={}
        S=s.split()
        k=[i for i in pattern]
        if len(S)!=len(k):
            return False
        for  j in range(len(S)):
            if k[j] not in ss and S[j] not in ss.values():
                ss[k[j]]=S[j]
                coun+=1
            elif  k[j] in ss:
                if ss[k[j]]==S[j]:
                    coun+=1
        return coun==len(S)


 