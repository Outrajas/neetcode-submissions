class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0 
        n=len(nums)-1
        while i<=n:
            mid=(i+n)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                i=mid+1
                continue
            if nums[mid]>target:
                n=mid-1
                continue
            break    
        return -1               

        