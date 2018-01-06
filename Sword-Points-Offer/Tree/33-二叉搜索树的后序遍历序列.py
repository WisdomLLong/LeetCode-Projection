'''
问题：看一个序列是否为二叉搜索树的后序遍历序列
注意：
1、二叉搜索树：左子树上的值都小于根节点的值，右子树上的值都大于根节点的值
2、数的遍历：
  1）由树到序列：广度、深度
  2）由序列到数：左右子树递归
'''


class Tree(object):
    def __init__(self, data, tleft, tright):
        self.tree = data
        self.tleft = None
        self.tright = None

class solution(object):
    def isPostorderOfBST(self, sequence):
        length = len(sequence)
        if sequence==None or length == 0:
            return False
        troot = sequence[-1]

        for i in range(length):
            if sequence[i] > troot:
                break
            
        for j in range(i, length):
            if sequence[j] < troot:
                return False
                
        left = True
        if i>0:
            left = self.isPostorderOfBST(sequence[:i])
            
        right = True
        if j<length-1:
            right = self.isPostorderOfBST(sequence[i:-1])
            
        return left and right
        
        
