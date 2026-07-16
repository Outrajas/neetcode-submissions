class MedianFinder:

    def __init__(self):
        self.lst=[]
    def addNum(self, num: int) -> None:
        self.lst.append(num)
        self.lst.sort()
    def findMedian(self) -> float:
        ln=len(self.lst)
        if ln%2!=0:
            return self.lst[((ln+1)//2) - 1 ]
        else:
            return (self.lst[(ln//2)] + self.lst[(ln//2)- 1])/2


        
        