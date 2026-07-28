class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_pointer=0
        cookies_pointer=0
        while child_pointer<len(g) and cookies_pointer <len(s):
            if s[cookies_pointer] >= g[child_pointer]:
                child_pointer+=1
            cookies_pointer+=1
        return child_pointer
            



        