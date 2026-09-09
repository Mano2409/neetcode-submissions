class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m=len(matrix)-1
        n=len(matrix[0])-1
        row=0
        column=n
        while row<=m and column>=0:
           
            if matrix[row][column]>target:
                column-=1
            elif matrix[row][column]==target:
                return True
            else:
                row+=1
        return False 