'''
环形链表是指，尾节点的下一个节点是链表中的某一个节点，形成了一个环
三个步骤：
1、求出环长：用两个速度不同的指针，当两者相遇的时候，相遇的节点一定在环中；以该节点为起点，一直绕一圈，求出环长
2、再利用两个指针找到环形入口。第一个指针先走一个环长，然后两个指针一起走，相遇的节点就是环形入口
'''


class ListNode(object):
    def __init__(self, data, nNode = None):
        self.value = data
        self.nextnode = nNode

class Solution(object):
    def meetingnode(self, nodehead):
        """
        :type s: str
        :rtype: bool
        """
        # 找到两个移速不同的指针指向相同位置的节点（此节点位于环中）
        if nodehead == None or nodehead.nextnode == None:
            return None
        pslow = nodehead
        pfast = nodehead
        while pslow!=None and pfast!=None:
            if pslow == pfast:
                return pfast
            pslow = pslow.nextnode
            pfast = pfast.nextnode
            if pfast.nextnode != None:
                pfast = pfast.nextnode
        return None
        
    def doorOfCircle(self, nodehead):
        meetnode = self.meetingnode(nodehead)
        if meetnode == None:
            return None
        
        # 找到环长
        clength = 1
        findnode = meetnode.nextnode
        while findnode != meetnode:
            clength += 1
            findnode = findnode.nextnode
        
        # 先移动PNode1，次数为环中节点的个数
        pnode1 = nodehead
        while clength != 0:
            pnode1 = pnode1.nextnode
            clength -= 1
        
        pnode2 = nodehead
        while pnode2 != pnode1:
            pnode2 = pnode2.nextnode
            pnode1 = pnode1.nextnode
            
        return pnode2
