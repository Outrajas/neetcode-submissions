class Solution:
    def anagram(self,s:str)->list:
        anagram=[0]*26
        for i in range(len(s)):
            anagram[ord(s[i])-97]+=1
        return anagram
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        val="" 
        if len(s1)==0:
            return True
        if len(s1)==1:
            if s1 in s2:
                return True
            return False    
        for i in range(len(s2)-len(s1)+1): 
            val=s2[i:i+len(s1)]
            if len(val)==len(s1):
                if self.anagram(val)==self.anagram(s1):
                    return True
        return False    



        