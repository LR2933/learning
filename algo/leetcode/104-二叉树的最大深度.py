# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        self.max_d = 0
 
        def dfs(r, c : int = 1):
            if r.left == None and r.right == None:
                self.max_d = max(c, self.max_d)
                return
            if r.left:
                dfs(r.left, c + 1)
            if r.right:
                dfs(r.right, c + 1)

        dfs(root)

        return self.max_d

