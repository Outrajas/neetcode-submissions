class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        j=1
        i=0
        while nums:
            if target-nums[i]==nums[j]:
                arr.append(i)
                arr.append(j)
                break
            if j==len(nums)-1:
                if i==len(nums)-2:
                   break   
                i=i+1
                j=i+1
                continue 
            j=j+1     
              

        return arr                   
          
                