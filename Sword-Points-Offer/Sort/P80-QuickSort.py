import random

class quickSort(object):
    def sortPart(self, data, start, end):
        if not isinstance(data, list) or start<0 or end>=len(data):
            print("Invalid Parameters") # 理论上应该抛出异常
            return
        
        index = random.randint(start, end)
        data[index], data[end] = data[end], data[index]
        
        small = start-1
        index = start
        while index < end:
            if data[index] < data[end]:
                small += 1
                if small != index:
                    data[index], data[small] = data[small], data[index]
            index += 1
        '''
        for index in range(index, end):
        '''
        small += 1
        data[small], data[end] = data[end], data[small]

        return small

    def sortAll(self, data, start, end):
        if start == end:
            return
        index = self.sortPart(data, start, end)
        if index > start :
            self.sortAll(data, start, index-1)
        if index < end:
            self.sortAll(data, index+1, end)
            
    def backData(self):
        print(self.data)
        
        
              
a = [5,4,6,3,23,6,3,4]
quickSort().sortAll( a, 0, len(a)-1)
print(a)    
'''
为什么可以直接打印a，sortAll都没有返回。
因为a是一个类的实例，而不是一个简单的数据类型int。
sortAll函数的data是一个指向这个实例的指针
'''



