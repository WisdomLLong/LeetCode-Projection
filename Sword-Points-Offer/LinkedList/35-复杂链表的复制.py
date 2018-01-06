'''
注意：
1、复杂链表，每一个节点不但有一个指向后面节点的指针，也有一个指向任一节点的指针
2、复制三步走：
    对于原链表中的每一个节点都复制一个在后面
    再对克隆的节点的PSibling进行赋值
    拆分成两条链表
'''

class ListNode(object):
    def __init__(self, data, nNode = None, pNode = None):
        self.value = data
        self.nextnode = nNode
        self.pSibling = pNode

class solution(object):
    def cloneLinkedList(self, lroot):
        self.cloneNode(lroot)
        self.clonepSibling(lroot)
        return self.splitList(lroot)
        
    def cloneNode(self, lroot):
        cloneNext = lroot
        while cloneNext.nextnode != None:
            cloneOfNode = ListNode(cloneNext.value, cloneNext.nextnode)
            cloneNext.nextnode = cloneOfNode
            cloneNext = cloneOfNode.nextnode
            
    def clonepSibling(self, lroot):
        cloneNext = lroot
        while cloneNext.nextnode != None:
            if cloneNext.pSibling != None:
                cloneNext.nextnode.pSibling = cloneNext.pSibling.nextnode
            cloneNext = cloneNext.nextnode
            
    def splitList(self, lroot):
        lrootClone = lroot.nextnode
        while lroot.nextnode != None:
            lroot_save = lroot.nextnode
            lroot.nextnode = lroot_save.nextnode
            lroot = lroot_save
        return lrootClone
