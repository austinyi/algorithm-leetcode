class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transposing aligns the axes of the matrix to prepare for rotation.
        # Reversing rows reflects the matrix to complete the 90-degree rotation.

        n = len(matrix)

        # transpose
        for i in range(n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

        return matrix

    # def rotate(self, matrix: List[List[int]]) -> None:
    #     n = len(matrix[0])
    #     for i in range(n // 2 + n % 2):
    #         for j in range(n // 2):
    #             tmp = matrix[n - 1 - j][i]
    #             matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
    #             matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
    #             matrix[j][n - 1 - i] = matrix[i][j]
    #             matrix[i][j] = tmp
