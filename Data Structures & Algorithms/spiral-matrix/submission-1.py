class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        left, right = 0, m - 1
        top, bottom = 0, n - 1
        new_list = []

        while top <= bottom and left <= right:
            # right
            for i in range(left, right + 1):
                new_list.append(matrix[top][i])
            top += 1

            # down
            for j in range(top, bottom + 1):
                new_list.append(matrix[j][right])
            right -= 1

            # left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    new_list.append(matrix[bottom][i])
                bottom -= 1

            # up
            if left <= right:
                for j in range(bottom, top - 1, -1):
                    new_list.append(matrix[j][left])
                left += 1

        return new_list