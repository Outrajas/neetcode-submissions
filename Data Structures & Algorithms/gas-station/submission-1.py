class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        j=0
        for i in range(n):
            j=i
            currgas=0
            while True:
                currgas=currgas+gas[j]-cost[j]
                if currgas<0:
                    break  
                j = (j + 1) % n    
                if j==i:
                    return i   
        return -1            


        