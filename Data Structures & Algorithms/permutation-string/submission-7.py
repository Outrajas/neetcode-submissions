class Solution:
    def anagram(self,s:str)->list:
        anagram=[0]*26
        for ch in s:
            anagram[ord(ch)-97]+=1
        return anagram
    def checkInclusion(self, s1: str, s2: str) -> bool:
        val="" 
        if len(s1)==0:
            return True
        if len(s1)==1:
            if s1 in s2:
                return True
            if len(s1)>len(s2):
                return False  
            return False   
        temp=self.anagram(s1)
        for i in range(len(s2)-len(s1)+1): 
            val=s2[i:i+len(s1)]
            if len(val)==len(s1):
                if self.anagram(val)==temp:
                    return True
        return False    



        