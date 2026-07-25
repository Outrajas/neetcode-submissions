class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        work=sorted(intervals)
        mappedhash={}
        ans=[-1]*len(queries)
        for i in range(len(queries)):
            temp=[]
            for j in range(len(work)):
                if queries[i]>work[j][1] or queries[i]<work[j][0] :
                    continue 
                temp.append(work[j][1]-work[j][0]+1)    
            if len(temp)==0:
                continue
            else:
                ans[i]=min(temp)   
        return ans             



        