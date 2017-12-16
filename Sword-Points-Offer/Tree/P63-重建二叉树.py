''''' 
重建二叉树 
题目描述 
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。 
'''  

class Tree(object):
    def __init__(self, data, tleft, tright):
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


#############################################################
# Better Solution 
# 实现了构造二叉树，打印二叉树的操作
#############################################################
class BTree:  
    ''''' 
    Represent a no in a binary tree. 
    '''  
    def __init__(self, c='/0', l=None, r=None):  
        ''''' 
        Initializes the node's data 
        '''  
        self.e = c  
        self.left = l  
        self.right = r  
def preorderTraverse(bt):  
    ''''' 
    返回前序遍历结果 
    '''  
    if bt:  
        return '%s%s%s' % (bt.e, preorderTraverse(bt.left), preorderTraverse(bt.right))  
        #@@ 第一个return返回的是一组字符串
    return ''  
    #@@ 第二个return返回''是因为，如果 if bt 不成立，返回一个空的字符串
def inorderTraverse(bt):  
    ''''' 
    返回中序遍历结果 
    '''  
    if bt:  
        return '%s%s%s' % (inorderTraverse(bt.left), bt.e, inorderTraverse(bt.right))  
    return '';  
def postorderTraverse(bt):  
    ''''' 
    返回后序遍历结果 
    '''  
    if bt:  
        return '%s%s%s' % (postorderTraverse(bt.left), postorderTraverse(bt.right), bt.e)  
    return ''  
def printBTree(bt, depth):  
    ''''' 
    递归打印这棵二叉树，*号表示该节点为NULL 
    '''  
    ''''' 
    if not bt: 
        ch = '*' 
    else: 
        ch = bt.e 
    '''  
    #ch=(lambda x: (x and x.e) or '*')(bt)  
    ch = bt.e if bt else '*'  
    if(depth > 0):  
        print '%s%s%s' % ((depth - 1) * '  ', '--', ch)  
    else:  
        print ch  
    if not bt:  
        return  
    printBTree(bt.left, depth + 1)  
    printBTree(bt.right, depth + 1)  
def buildBTreeFromPreIn(preo, ino):  
    ''''' 
    根据前序和中序遍历结果重构这棵二叉树 
    '''  
    if(preo == '' or ino == ''):  
        return None  
    pos = ino.find(preo[0])  
    if(pos < 0):  
        return None          
    return BTree(preo[0], buildBTreeFromPreIn(preo[1:pos + 1], ino[0:pos]), buildBTreeFromPreIn(preo[pos + 1:], ino[pos + 1:]))  
    #return nd  
def buildBTreeFromInPost(ino, po):  
    ''''' 
    根据中序和后序遍历结果重构这棵二叉树 
    '''  
    if(ino == '' or po == ''):  
        return None  
    pos = ino.find(po[-1])  
    if(pos < 0):  
        return None     
    return BTree(po[-1], buildBTreeFromInPost(ino[0:pos], po[0:pos]), buildBTreeFromInPost(ino[pos + 1:], po[pos:-1]))  
      
if __name__ == '__main__':  
    preo = 'ABDGCEFH'  
    ino = 'DGBAECHF'  
    po = 'GDBEHFCA'  
    bt = buildBTreeFromPreIn(preo, ino)  
    print 'Build from preorder & inorder'  
    print 'Preorder: %s' % (preorderTraverse(bt))  
    print 'Inorder: %s' % (inorderTraverse(bt))  
    print 'Postorder: %s' % (postorderTraverse(bt))  
    print 'The BTree is (* means no such a node):'  
    printBTree(bt, 0)  
    bt = buildBTreeFromInPost(ino, po)  
    print 'Build from inorder & postorder'  
    print 'Preorder: %s' % (preorderTraverse(bt))  
    print 'Inorder: %s' % (inorderTraverse(bt))  
    print 'Postorder: %s' % (postorderTraverse(bt))  
    print 'The BTree is (* means no such a node):'  
    printBTree(bt, 0)  
