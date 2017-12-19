'''
问题：从矩阵中找到一个字符串的路径是否存在
思路：深度优先搜索
'''

############################################
# Better Solution 1 深度优先搜索
############################################
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == "":
            return True
        if len(board) == 0:
            return False
        visited = [[0] * len(board[0]) for i in range(0, len(board))]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j, board, visited, word, index):
            if word[index] != board[i][j]:
                return False
            if len(word) - 1 == index:
                return True
            for direction in directions:
                # 为什么这里不是深度优先，因为for循环是一个一个进行的，当一条路径走通的时候，就会return TRUE
                ni, nj = i + direction[0], j + direction[1]
                if ni >= 0 and ni < len(board) and nj >= 0 and nj < len(board[0]):
                    if visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        if dfs(ni, nj, board, visited, word, index + 1):
                            return True
                        visited[ni][nj] = 0
            return False
            
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                visited[i][j] = 1
                if dfs(i, j, board, visited, word, 0):
                    return True
                visited[i][j] = 0
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
