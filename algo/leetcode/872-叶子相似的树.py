# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def f(r :TreeNode, l: List):
            if r == None:
                return
            elif r.left == None and r.right == None:
                l.append(r.val)
            f(r.left, l)
            f(r.right, l)
            return l

        if f(root1, []) == f(root2, []):
            return True
        return False

