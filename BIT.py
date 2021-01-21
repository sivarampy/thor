class BIT:
    def __init__(self):
        self.__list = [3,5,-1,10,5,9,-3,19,7,9,3]

    def getParent(self,index):
        comTemp = ~ index
        temp2 = comTemp + 1
        temp3 = index & temp2
        parent = index - temp3
        return parent

    def getNext(self,index):
        comTemp = ~ index
        temp2 = comTemp + 1
        temp3 = index & temp2
        next = index + temp3
        return next

    def sumOfN(self,n): ## sum of first n numbers
        ans = self.__list[n-1]
        parent = self.getParent(n)
        while parent != 0:
            ans += self.__list[parent-1]
            parent = self.getParent(parent)
        return ans

    def rangeSum(self,high,low = 0): 
        if low != 0:
            ans = self.sumOfN(high)-self.sumOfN(low)
            return ans
        else:
            return self.sumOfN(high)

b = BIT()
n = 5
m = 2 
print(b.rangeSum(n,m)) 
