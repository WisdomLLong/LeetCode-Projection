'''
P134
要求只遍历列表一次，可以想到，每次遍历可以“存储两个值”，因此用两个指针
'''


class ListNode(object):
    def __init__(self, data, nNode = None):
        self.value = data
        self.nextnode = nNode

class Solution(object):
    def findKthNodeToTail(self, nodehead, k):
        """
        :type s: str
        :rtype: bool
        """
        if nodehead.value == None:
            return None
            
        upnode = nodehead
        downnode = nodehead
        kk = 1
        while  kk < k:
            if downnode.nextnode == None:
                return False
            downnode == downnode.nextnode
            kk += 1
        
        while downnode.nextnode != None:
            downnode == downnode.nextnode
            upnode = upnode.nextnode
        
        return upnode
            
        
                
print(Solution().changeStation("63452849546385"))
