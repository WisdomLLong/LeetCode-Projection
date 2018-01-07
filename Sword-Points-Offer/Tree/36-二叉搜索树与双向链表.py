'''
P191
问题：
1、实现二叉搜索树变为双向链表（数据类型不用变），双向链表是已经排序的
注意：
1、也就是数的中序遍历
'''

class Tree(object):
    def __init__(self, data, tleft=None, tright=None):
        self.tree = data
        self.tleft = None
        self.tright = None

        
class solution(object):
    def convert(self, troot):
        tLastNodeInList = Tree(None) 
        self.convertNode(troot, tLastNodeInList)
        
        while tLastNodeInList.tleft != None:
            tLastNodeInList = tLastNodeInList.tleft
        
        return tLastNodeInList
        
        
    def convertNode(self, troot, tLastNodeInList):
        if troot == None:
            return
            
        tcurrent = troot
        
        if tcurrent.tleft != None:      # 寻找左子树
            self.convertNode(tcurrent.tleft, tLastNodeInList)
            
        tcurrent.tleft = tLastNodeInList       # tLastNodeInList表示左子树最大值
        if tLastNodeInList != None:     # 双向交换
            tLastNodeInList.tright = tcurrent
            
        tLastNodeInList = tcurrent      # tLastNodeInList时刻指向最大值
        
        if tcurrent.tright != None:
            self.convertNode(tcurrent.tright, tLastNodeInList)
            
            
        
        
                
                
                
