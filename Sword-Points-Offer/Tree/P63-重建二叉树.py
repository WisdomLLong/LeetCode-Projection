''''' 
重建二叉树 
题目描述 
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。 
'''  

class Tree(object):
    def __init__(self, data):
        self.tree = data
        self.tleft = None
        self.tright = None
        
class TwoTree(object):
    def reConstructBinaryTree(self, pre, tin):
        if len(pre)==0:
            return None
        if len(pre)==1:
            return Tree(pre[0])
        else:
            res = Tree(pre[0])
            res.tleft = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1], tin[:tin.index(pre[0])])
            res.tright = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])
        return res   
root = TwoTree().reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
#@@ 注意这里的root得到的返回值是根节点res，其他节点也返回了，只是作为tleft和tright返回的。
