class Solution:
    def hammingWeight(self, n: int) -> int:
        n=format(n, '032b')
        temp=list(map(int, str(n)))
        count=0
        for i in temp:
            if i==1:
                count+=1
        return count        
        