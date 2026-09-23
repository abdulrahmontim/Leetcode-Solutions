# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return
        
        if not preorder: return
        root = TreeNode(preorder[0])
        while inorder or preorder:
            # take root from preorder
            # section the root using inorder
            #pass the sections to build
            middle = inorder.index(root.val)
            root.left = self.buildTree(preorder[1: middle+1], inorder[:middle])
            root.right = self.buildTree(preorder[middle+1:], inorder[middle+1:])
            return root