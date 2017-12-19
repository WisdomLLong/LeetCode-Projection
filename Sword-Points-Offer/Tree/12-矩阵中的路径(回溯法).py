'''
问题：从矩阵中找到一个字符串的路径是否存在
思路：深度优先搜索
'''

############################################
Better Solution 1 广度优先搜索，容易超时
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
