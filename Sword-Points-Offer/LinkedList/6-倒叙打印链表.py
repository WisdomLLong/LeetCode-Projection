
# 后进先出的思路也可以用栈

#####################################################
# 倒叙打印链表数据: nodePrint_reverse()
#####################################################
def nodePrint_reverse(self, lhead):
        if lhead.next:
            self.nodePrint_reverse(lhead = lhead.next)
        print(lhead.data)
