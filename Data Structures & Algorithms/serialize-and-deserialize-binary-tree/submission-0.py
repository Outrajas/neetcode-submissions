# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        lst=[]
        def ser(node):
            if not node:
                lst.append(None)
                return 
            lst.append(node.val)    
            ser(node.left)    
            ser(node.right) 
            return lst
        ser(root)    
        return "|".join(str(x) for x in lst)   
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data)==0:
            return None
        results=[]
        for c in data.split("|"):
            if c=="None":
                results.append(None)
                continue
            results.append(int(c))   
        def build(preorder):
                val = preorder.pop(0)
                if val is None:
                    return None
                node = TreeNode(val)
                node.left = build(preorder)
                node.right = build(preorder)
                return node
        return build(results)        











