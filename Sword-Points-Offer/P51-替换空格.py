'''
如何在每个字符只移动一次的情况下，即将"We are happy" 变为 "We%20are%20happy"
'''
思路：倒着移动
####################################################################
Solution
####################################################################
import heapq
class Solution(object):
    def findMedianSortedArrays(self, xx):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: float
        """
        # 统计空格数
        xx_l = list(xx)
        length = 0
        for x in xx_l:
            if x==' ':
                length += 1
        
        # 扩展到合适的存储空间
        for l in range(2*length):
            xx_l.append(' ')
            
        # 从后到前插入%20,首先定义两个指针
        p1, p2 = len(xx)-1, len(xx_l)-1
        while p1>=0:
            if xx_l[p1]!=' ' and xx_l[p1+1]==' ':
                xx_l[p2] = xx_l[p1]
                xx_l[p1] = ' '
                p1 -= 1
                p2 -= 1
            elif xx_l[p1]==' ' and xx_l[p1-1]!=' ':
                xx_l[p2] = '0'
                xx_l[p2-1] = '2'
                xx_l[p2-2] = '%'
                p2 -= 3
                p1 -= 1
            else:
                p1 -= 1
          
        #return ''.join(xx_l)
        return xx_l

b = Solution()
print(b.findMedianSortedArrays("We are happy"))
