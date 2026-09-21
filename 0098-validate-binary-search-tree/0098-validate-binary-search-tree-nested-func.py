# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validateRange(root, min_val, max_val):
            if not root:
                return True
            
            if not (min_val < root.val < max_val):
                return False
            return validateRange(root.left, min_val, root.val) and validateRange(root.right, root.val, max_val)
        
        return validateRange(root, -float("inf"), float("inf"))
    
        
