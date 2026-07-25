class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        prod=1 
        if n<0:
            for i in range((-n)//2):
                prod=prod/x 
            if n%2!=0:
                return (prod**2)/x     
        else:        
            for i in range(n//2):
                prod=x*prod
            if n%2!=0:
                return (prod**2)*x    
        return prod**2    
        