class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        for ch in arr:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        ans=[]
        for key,values in freq.items():
            if key==values:
                ans.append(values)
        if ans:
            return max(ans)
        return -1                        