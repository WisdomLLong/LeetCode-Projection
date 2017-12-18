'''
！！！排序数组或者排序数组的旋转，通过二分法实现O(logn)的时间效率
特殊情况：
'''


class xzmin(object):
    def mmin(self, data):
        if len(data)==0:
            return
        if len(data)==1:
            return data[0]
        
        index1 = 0
        index2 = len(data) - 1
        while index1 < index2:
            indexmin = int((index1+index2)/2)
            # if data[indexmin] == data[index1] and data[indexmin] == data[index2]:
            # 以上这种情况下二分法无法实现，需要顺序查找
            if data[indexmin] >= data[index1]:
                index1 = indexmin
            else:
                index2 = indexmin
            if index2-index1==1:
                indexmin = index2
                break
        return data[indexmin]

print(xzmin().mmin([3,4,5,6,1,2]))
