class Solution:
    def getSum(self, a: int, b: int) -> int:

        if b == 0:
            return a
        mask = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF
        cur = 0
        while b != 0:
            cur = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = cur
            b = carry
        
        return cur if cur <= maxInt else ~(cur ^ mask)