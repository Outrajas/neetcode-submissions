class WordDictionary:

    def __init__(self):
        self.words=[]
    def addWord(self, word: str) -> None:
        if word in self.words:
            return
        self.words.append(word)    
    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        l=len(word)
        for w in self.words:
            if l!=len(w):
                continue
            match=True
            for a,b in zip(word,w):
                if a != b and a != '.':
                    match = False
                    break
            if match:   
                return True     
        return False                    


        
