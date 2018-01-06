'''
注意：
1、前序，中序，后序3种遍历方式中，只有前序遍历是首先访问根节点
2、注意对于不成立的路径，递归后删除不成立的节点
'''

class Tree(object):
    def __init__(self, data, tleft, tright):
        self.tree = data
        self.tleft = None
        self.tright = None

class solution(object):
    def findPath(self, troot, expectedSum):
        if troot == None:
            return False
        path = []
        currentSum = 0
        self.toFindPath(troot, expectedSum, path, currentSum)
        
    def toFindPath(self, troot, expectedSum, path, currentSum):
        currentSum += troot.tree
        path.append(troot)
        isLeaf = troot.tleft==None and troot.tright==None
                
        if isLeaf and currentSum == expectedSum:
            print('A path is found:')
            for i in path:
                print(i.tree)
        print('\n')
        
        if troot.tleft != None:
            self.toFindPath(troot, expectedSum, path, currentSum)
        if troot.tright != None:
            self.toFindPath(troot, expectedSum, path, currentSum)
            
        path.pop(-1)
        '''
        这个用的很精华，递归函数前面的是 终止条件 和 一些操作条件
        递归函数后面的是，递归函数返回后需要做的事情
        '''
        
