# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 0

        def dfs(r, c = 0):
            c = c << 1
            c = c | r.val
            if not r.right and not r.left:
                self.ans += c

            if r.left:
                dfs(r.left, c)

            if r.right:
                dfs(r.right, c)

        dfs(root)
        return self.ans
        
