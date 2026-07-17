class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        work=sorted(stones)
        while len(work)>1:
            if len(work)==2:
                ans=work[1]-work[0]
                break
            if work[-1]==work[-2]:
                work.pop()
                work.pop()
                continue 
            temp=work[-1]-work[-2]
            work.pop()
            work.pop()
            work.append(temp) 
            work.sort()   
        if len(work) == 1:
            return work[0]       
        return ans    

            
        