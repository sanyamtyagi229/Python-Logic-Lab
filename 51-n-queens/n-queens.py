
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        def isSafe(row, col):

            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False

                i -= 1
                j -= 1
            i = row - 1
            j = col + 1

            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False

                i -= 1
                j += 1

            return True

        def solve(row):

            # Base case
            if row == n:
                ans.append([''.join(r) for r in board])
                return

            for col in range(n):

                if isSafe(row, col):

                    board[row][col] = 'Q'

                    solve(row + 1)

                    board[row][col] = '.'

        solve(0)

        return ans
