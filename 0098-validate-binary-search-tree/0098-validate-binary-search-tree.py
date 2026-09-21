# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.validateRange(root, -float("inf"), float("inf"))
    
    def validateRange(self, root: TreeNode | None, min_val: int, max_val: int) -> bool:
        if not root:
            return True
        
        if not (min_val < root.val < max_val):
            return False
        
        return self.validateRange(root.left, min_val, root.val) and self.validateRange(root.right, root.val, max_val)
