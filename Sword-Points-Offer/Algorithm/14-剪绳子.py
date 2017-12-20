'''
P96
动态规划问题：如果一个问题可以被拆解为多个小问题，且这些小问题又会出现重叠，则采用自下而上的“递归方法”求解
'''


class Solution:
    def maxProductAfterCutting(self, length):
        if length <= 1:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        save = [0, 1, 2, 3]+[0]*(length-3)  # 
        for i in range(4, length+1):    # 注意range是左闭右开的
            mmax = 0
            for j in range(1, i//2):
                if mmax < save[j]*save[i-j]:
                    mmax = save[j]*save[i-j]
            save[i] = mmax
        return save[-1]

        
length = 8
print(Solution().maxProductAfterCutting(length))
