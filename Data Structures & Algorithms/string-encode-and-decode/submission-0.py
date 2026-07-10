class Solution:
    def asc(self,string:str)->str:
        enc=""
        for i in range(len(string)):
            enc=enc+str(ord(string[i]))+'.'
        return enc

    def deasc(self,string:str)->str:  
        ans=""
        word=""
        for i in range(len(string)):
            if string[i]!='.':
               word=word+string[i]
            if string[i]=='.':
                s=int(word)
                ans=ans+chr(s)
                word=""
                continue
        return ans       
    def encode(self, strs: List[str]) -> str:
        enc_string=""
        for i in range(len(strs)):
            enc_string=enc_string+str(self.asc(strs[i]))+'_'
        return enc_string    

    def decode(self, s: str) -> List[str]:
        dec_string=[]
        word=""
        for i in range(len(s)):
            if s[i]!='_':
                word=word+s[i]
            if  s[i]=='_':
                dec_string.append(self.deasc(word))  
                word=""
                continue
        return dec_string
                

            



