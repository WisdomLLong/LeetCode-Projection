'''
问题：实现二叉树的左子树与右子树的交换
注意：
这里并没有return，但仍然是递归，因为其实每一层的交换是独立进行的，与下面的层没有关系
'''

class Tree(object):
    def __init__(self, data, tleft, tright):
        self.value = data
        self.tleft = None
        self.tright = None

class Solution(object):
    def exchangeLeftandRight(self, proot):
        """
        :type s: str
        :rtype: bool
        """
        if proot == None:
            return
        if proot.tleft == None and proot.tright == None:
            return
        proot.tleft, proot.tright = proot.tright, proot.tleft
        if proot.tleft:
            self.exchangeLeftandRight(proot.tleft)
        if proot.tright:
            self.exchangeLeftandRight(proot.tright)
