class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        temp=[target-x for x in numbers]
        for i in range(len(numbers)):
            if numbers[i] in temp:
                ans.append(i+1)
                key=temp.index(numbers[i])
                ans.append(key+1)
                break
        return ans        




