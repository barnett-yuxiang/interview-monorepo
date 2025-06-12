
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
#    / \ /
#   8  9 10
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)

# Traversal:
# DFS - pre-order; in-order; post-order;
# BFS - level-order

def dfs_preorder(node: TreeNode):
    # 1,2,4,8,5,9,3,6,7,10
    pass

def dfs_inorder(node: TreeNode):
    pass

def dfs_postorder(node: TreeNode):
    pass

def bfs_levelorder(node: TreeNode):
    pass
