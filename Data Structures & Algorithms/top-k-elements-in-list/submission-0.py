class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ke=list(set(nums))
        counts=defaultdict(int)
        for num in nums:
            if num in ke:
                counts[num]+=1
        return sorted(counts,key=counts.get, reverse=True)[:k]       
            
