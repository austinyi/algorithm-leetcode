class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {}
        for m in range(9):
            for n in range(9):
                if board[m][n] != '.':
                    if board[m][n] in d:
                        for i,j in d[board[m][n]]:
                            if i == m or j == n:
                                return False
                            if i // 3 == m // 3 and j // 3 == n // 3:
                                return False
                        d[board[m][n]].append((m,n))
                    else:
                        d[board[m][n]] = [(m,n)]
        return True


        # for m in range(9):
        #     for n in range(9):
        #         if board[m][n] != ".":
        #             if board[m][n] in board[m][:n] + board[m][n+1:]:
        #                 return False
        #             col = [row[n] for row in board[:m] + board[m+1:]]
        #             if board[m][n] in col:
        #                 return False
                
        # for m in range(3):
        #     for n in range(3):
        #         a = set()
        #         for i in range(3):
        #             for j in range(3):
        #                 if board[3*m+i][3*n+j] != ".":
        #                     if board[3*m+i][3*n+j] in a:
        #                         return False
        #                     else:
        #                         a.add(board[3*m+i][3*n+j])
        # return True
