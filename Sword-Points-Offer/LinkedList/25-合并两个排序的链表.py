'''
问题：合并两个排序的链表，使得新的链表仍然是有序的
注意：
1、链表可能会断
'''

###############################################################
# My solution 没有使用递归，没有验证正误
###############################################################
class ListNode(object):
    def __init__(self, data, nNode = None):
        self.value = data
        self.nextnode = nNode

class Solution(object):
    def combineTwoSortedLinkedList(self, nodehead1, nodehead2):
        """
        :type s: str
        :rtype: bool
        """
        if nodehead1.value == None and nodehead2.value != None:
            return nodehead2
        if nodehead1.value != None and nodehead2.value == None:
            return nodehead1
        if nodehead1.value == None and nodehead2.value == None:
            return None
        
        if nodehead1.value > nodehead2.value:
            newnodehead = nodehead1
        else:
            newnodehead = nodehead2
            
        while nodehead1 != None and nodehead2 != None:
            if nodehead1.value > nodehead2.value:
                nodehead1.nextnode, nodehead1 = nodehead2, nodehead1.nextnode
            else:
                nodehead2.nextnode, nodehead2 = nodehead1, nodehead2.nextnode
                
        return newnodehead

###############################################################
# Better solution 使用了递归，思路清晰
###############################################################
class ListNode(object):
    def __init__(self, data, nNode = None):
        self.value = data
        self.nextnode = nNode

class Solution(object):
    def combineTwoSortedLinkedList(self, nodehead1, nodehead2):
        """
        :type s: str
        :rtype: bool
        """
        if nodehead1 == None:
            return nodehead2
        elif nodehead2 == None:
            return nodehead1
            
        pMergedHead = None
        
        if nodehead1.value < nodehead2.value:
            pMergedHead = nodehead1
            pMergedHead.nextnode = self.combineTwoSortedLinkedList(nodehead1.nextnode, nodehead2)
        else:
            pMergedHead = nodehead2
            pMergedHead.nextnode = self.combineTwoSortedLinkedList(nodehead1, nodehead2.nextnde)
            
        return pMergedHead
