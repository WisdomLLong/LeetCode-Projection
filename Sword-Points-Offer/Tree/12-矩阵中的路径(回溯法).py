'''
问题：从矩阵中找到一个字符串的路径是否存在
思路：深度优先搜索
'''

############################################
# Better Solution 1 深度优先搜索_1
############################################
class Solution:
    def exist(self, board, word):
        visited = [[False for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and self.dfs(board, word, i, j, 0, visited):
                    return True
        return False

    def dfs(self, board, word, i, j, idx, visited):
        if idx == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx] or visited[i][j]:
            return False

        visited[i][j] = True
        up = self.dfs(board, word, i-1, j, idx+1, visited)
        down = self.dfs(board, word, i+1, j, idx+1, visited)
        left = self.dfs(board, word, i, j-1, idx+1, visited)
        right = self.dfs(board, word, i, j+1, idx+1, visited)
        # 这样岂不是广度优先？测试了与深度优先的耗时竟然相同
        if up or down or left or right:
            return True

        visited[i][j] = False
        return False
    
############################################
# Better Solution 2 广度优先搜索，容易超时
############################################
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        xx = []
        for i in range(len(board)):
            xx += board[i]
        row = len(board)
        col = len(board[0])
        word = list(word)
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and self.visit([(i, j)], xx, row, col, word):
                    return True
        return False
    
    def visit(self, path, matrix, row, col, data):
        if len(path)==len(data):
            return True
        i, j = path[-1]
        nex = [(ii, jj) for ii, jj in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)] 
               if 0<= ii < row and 0<= jj <col and 
               (ii, jj) not in path 
               and matrix[ii*col + jj]==data[len(path)]]
        return sum([self.visit(path+[x], matrix, row, col,data) for x in nex])
        # 虽然这里也是用了for循环，但他是深度优先搜索，因为这里有一个列表生成器，每一个生成器都是要执行的。
        '''
        for x in nex:
            if self.dfs_bfs(path+[x], matrix, row, col,data):
                return True
        '''
        #上面这个是深度优先搜索，不会超时
    
