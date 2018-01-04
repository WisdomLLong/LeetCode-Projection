'''
问题：以各种方式打印树
注意：
1、熟练掌握广度优先搜索和深度优先
'''
###########################################################
# P174
###########################################################
class Tree(object):
    def __init__(self, data, tleft, tright):
        self.tree = data
        self.tleft = None
        self.tright = None

class solution(object):
    def printTreeByLine(self, troot):
        if troot == None:
            return
        printList = []
        toBePrinted = 1
        nextLine = 0
        printList.append(troot)
        while len(printList) != 0:
            toPrintNode = printList.pop(0)
            print(toPrintNode.value)
            toBePrinted -= 1
            if toPrintNode.tleft:
                printList.append(toPrintNode.tleft)
                nextLine += 1
            if toPrintNode.tright:
                printList.append(toPrintNode.tright)
                nextLine += 1
            if toBePrinted == 0:
                print('\n')
                toBePrinted, nextLine = nextLine, 0

                
##########################################################
# P176 S形打印树的值
##########################################################
class Tree(object):
    def __init__(self, data, tleft, tright):
        self.tree = data
        self.tleft = None
        self.tright = None

class solution(object):
    def printTreeByS(self, troot):
        # 利用两个栈来存储树的两行
        if troot == None:
            return
        twoLine = [[], []]
        currentLine = 0
        nextLine = 1
        twoLine[currentLine].append(troot)
        
        while len(twoLine[currentLine])!=0 or len(twoLine[nextLine])!=0:
            toPrint = twoLine[currentLine].pop(0)
