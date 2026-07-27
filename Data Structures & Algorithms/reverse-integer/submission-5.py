class Solution:
    def reverse(self, x: int) -> int:
        if x==0 :
            return 0       
        c=False
        if x<0:
            c=True
        num=str(abs(x))
        num=num[::-1]
        num=int(num)
        if num>2147483647:
            return 0 
        if c==True:
            return (-1)*num
        return num    


        