class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index=0
        count=0
        for i in range(len(mat)):
            c=mat[i].count(1)
            if c>count:
                count=c
                index=i
        return [index,count]