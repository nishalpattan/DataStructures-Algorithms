class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        TC : O(m * n)
        SC : O(m * n)
        m --> # rows
        n --> # cols
        """
        if board == []:
            return None
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                self.dfs(i, j, board)
        for i in range(len(board)):
            for j in [0, len(board[0]) - 1]:
                self.dfs(i, j, board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == ".":
                    board[i][j] = "O"

    def dfs(self, row, col, board):
        if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == "O":
            board[row][col] = "."
            self.dfs(row - 1, col, board)
            self.dfs(row + 1, col, board)
            self.dfs(row, col - 1, board)
            self.dfs(row, col + 1, board)