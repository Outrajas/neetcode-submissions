class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp="".join(str(x) for x in digits)
        curr=str(int(temp)+1)
        ans=[x for x in curr]
        return ans



