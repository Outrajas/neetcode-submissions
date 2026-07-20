class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = True
            node['word'] = word
        
        rows, cols = len(board), len(board[0])
        res = []
        
        def dfs(i, j, node):
            ch = board[i][j]
            if ch not in node:
                return
            node = node[ch]
            if '#' in node:
                res.append(node['word'])
                del node['#']
                del node['word']
            
            board[i][j] = '#'
            if i > 0: dfs(i-1, j, node)
            if i < rows-1: dfs(i+1, j, node)
            if j > 0: dfs(i, j-1, node)
            if j < cols-1: dfs(i, j+1, node)
            board[i][j] = ch
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie)
        
        return res