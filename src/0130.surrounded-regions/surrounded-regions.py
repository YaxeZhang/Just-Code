from collections import deque

class Solution:
    
    def bfs(self, board, start_i, start_j):
        m, n = len(board), len(board[0])
        
        q = deque()
        q.append((start_i,start_j))
        
        while q:
            i, j = q.popleft()
            
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 's'
                q.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])
                
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        
        # go round the border and run bfs from every 'O' found, those 'O's found
        # by the bfs stay - encoded 's'
        m, n = len(board), len(board[0])
        
        
        for i in range(m):
            if board[i][0] == 'O':
                self.bfs(board, i, 0)
            if board[i][n-1] == 'O':
                self.bfs(board, i, n-1)
                
        for j in range(n):
            if board[0][j] == 'O':
                self.bfs(board, 0, j)
            if board[m-1][j] == 'O':
                self.bfs(board, m-1, j)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 's':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
            