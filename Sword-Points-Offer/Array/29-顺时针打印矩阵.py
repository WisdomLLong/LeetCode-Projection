'''
注意：
可以画图，便于理解
'''
###########################################################
# Better Solution 
# 注意最后一行，返回的是数组的前半部分，因为其实前面的代码并不是很严谨，
# 最后会多打印一些内容
###########################################################
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix ==[]:
            return []
        if len(matrix)==0 and len(matrix[0])==0:
            return []
        ans = []
        
        up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        while up <= down and left <= right:
            for i in range(left, right+1):
                ans.append(matrix[up][i])
            up += 1
            for i in range(up, down+1):
                ans.append(matrix[i][right])
            right -= 1
            for i in range(right, left-1, -1):
                ans.append(matrix[down][i])
            down -= 1
            for i in range(down, up-1, -1):
                ans.append(matrix[i][left])
            left += 1
        return ans[:(len(matrix) * len(matrix[0]))]
        
        
print(Solution().spiralOrder([[2,3]]))
