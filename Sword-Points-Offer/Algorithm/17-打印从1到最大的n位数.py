'''
P114
相当于，把每一个位置上的数从0到9全排列一遍
递归 + 全排列
'''


class Solution:
    def print1ToMaxOfNDigits(self, n):
        if n<0:
            return
        number = ['0']*n
        self.Print1ToMaxOfNDigitsRecursively(number, n, 0)
        '''
        for i in range(10):
            number[0] = str(i)
            self.Print1ToMaxOfNDigitsRecursively(number, n, 0)
            '''
            
    def Print1ToMaxOfNDigitsRecursively(self, number, length, index):
        # if index == length-1:
        if index == length:
            self.PrintNumber(number,length)
            return
        for i in range(10):
            number[index] = str(i)
            # number[index+1] = str(i)
            self.Print1ToMaxOfNDigitsRecursively(number, length, index+1)
            
    def PrintNumber(self, number, length):
        printbumber = number
        for index in range(length):
            if printbumber[index] == '0':
                printbumber[index] = ''
            else:
                print( ''.join(printbumber))
                break
     
        
Solution().print1ToMaxOfNDigits(2)
