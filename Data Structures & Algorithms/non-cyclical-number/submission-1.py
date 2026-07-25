class Solution:
    
    def isHappy(self, n: int) -> bool:
        curr=n
        app=[]
        while True:
            temp=sum([int(d)**2 for d in str(curr)])
            if temp in app:
                return False
            if temp==1:
                return True
            app.append(temp)
            curr=temp 

        