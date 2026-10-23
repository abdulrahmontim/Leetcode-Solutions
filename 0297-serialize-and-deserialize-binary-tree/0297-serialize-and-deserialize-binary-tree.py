# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = list()

        def dfs(node):
            if node is None:
                tree.append("E")
                return

            tree.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(tree)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split(",")
        curr_idx = 0

        def dfs():
            nonlocal curr_idx
            if len(tree) <= 0: return TreeNode(None)
            curr_val = tree[curr_idx]
            curr_idx += 1

            if curr_val == "E":
                return None
            
            node = TreeNode(int(curr_val))
            node.left = dfs()
            node.right = dfs()
        
            return node
        
        return dfs()

            
        







# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))