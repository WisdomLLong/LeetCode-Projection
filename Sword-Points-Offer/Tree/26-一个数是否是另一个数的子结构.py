'''
问题：探究一个数是否被完全包含在另一个树中
注意：
1、递归在树中的编写，关键在边界条件（退出条件）的定义
2、计算机中的小数存储是有误差的，因此不能用恒等好来判断两个float的数是否相同
'''


class Tree(object):
    def __init__(self, data, tleft, tright):
        self.value = data
        self.tleft = None
        self.tright = None

class Solution(object):
    def hasSubtree(self, proot1, proot2):
        """
        :type s: str
        :rtype: bool
        """
        
        if proot1 != None and proot2 != None:
            if self.equal(proot1.value, proot2.value):
                result = self.tree1HasTree2(proot1, proot2)
            if not result:  # 递归很重要的一点就是找到终止条件
                result = self.hasSubtree(proot1.tleft, proot2)
            if not result:
                result = self.hasSubtree(proot1.tright, proot2)
                
        return result
                
    def tree1HasTree2(self, proot1, proot2):
        if proot2 == None:
            return True
        if proot1 == None:
            return False
        if not self.equal(proot1.value, proot2.value):
            return False
        return self.tree1HasTree2(proot1.tleft, proot2.left) and \
                self.hasSubtree(proot1.tright, proot2.tright)
                
    def equal(value1, value2):
        # 因为double数据类型的数据在极小位的时候是有误差的，因此只要差在一个范围内都认为是相同的
        if 0.0000001 < value1-value2 < 0.0000001:
            return True 
        else:
            return False
            
        
