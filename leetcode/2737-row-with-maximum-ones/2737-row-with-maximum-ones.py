class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count=0
        index=0
        for i in range(len(mat)):
            each=sum(mat[i])
            if each>count:
                count=each
                index=i

        return [index,count]
        