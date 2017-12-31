'''
问题：判断一个二叉树是否对称
方法：
判断它的 前序遍历 和 新的遍历方式（父节点，右子节点，左子节点）是否相同
'''


class Tree(object):
    def __init__(self, data, tleft, tright):
        self.value = data
        self.tleft = None
        self.tright = None

class Solution(object):
    
    def isSymmetrical_1(self, proot):
        return self.isSymmetrical_2(proot, proot)
        
    def isSymmetrical_2(self, proot1, proot2):
        if proot1 == None and proot2 == None:
            return True
        if proot1 == None or proot2 ==None:
            return False
        if proot1.value != proot2.value:
            return False
            
        return self.isSymmetrical_2(proot1.tleft, proot2.tright) and \
                self.isSymmetrical_2(proot1.tright, proot2.tleft)
                # 这里的proot1.tleft proot1.tright 就是前序遍历
                # proot2.tright proot2.tleft 就是新的遍历方式
