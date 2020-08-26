# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.lonely_nodes=[]
        def dfs(root):
            if not root:return 
            if root.left and not root.right:
                self.lonely_nodes.append(root.left.val)
            if root.right and not root.left:
                self.lonely_nodes.append(root.right.val)
            
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
                
        dfs(root)
        return self.lonely_nodes