'''
归并排序
时间：O(nlog2n)
空间：O(n)
'''

class Solution:
    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        if i < len(left):
            result += left[i:]
        if j < len(right):
            result += right[j:]
        return result
    
    def mergeSort(self, data):
        if len(data) == 1:
            return data
        helf = len(data)//2
        left = self.mergeSort(data[:helf])
        right = self.mergeSort(data[helf:])
        return self.merge(left, right)

        
print(Solution().mergeSort([4,76,3,6,3,7,2,9]))
