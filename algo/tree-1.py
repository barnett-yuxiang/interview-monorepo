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


# @pre-order: 1, 2, 4, 8, 9, 5, 10, 3, 6, 7
def dfs_preorder_v1(root: TreeNode):
    if not root:
        return

    print(root.val, end=", ")
    if root.left:
        dfs_preorder_v1(root.left)
    if root.right:
        dfs_preorder_v1(root.right)


def dfs_preorder_v2(root: TreeNode):
    if not root:
        return

    stack = [root]  # LIFO
    while stack:
        node = stack.pop()
        print(node.val, end=", ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


print("Pre-Order:")
dfs_preorder_v1(root)
print()
dfs_preorder_v2(root)
print()
print("------")
# @pre-order


# @in-order: 8, 4, 9, 2, 10, 5, 1, 6, 3, 7
def dfs_inorder_v1(root: TreeNode):
    if not root:
        return

    if root.left:
        dfs_inorder_v1(root.left)
    print(root.val, end=", ")
    if root.right:
        dfs_inorder_v1(root.right)


def dfs_inorder_v2(root: TreeNode):
    if not root:
        return

    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.val, end=", ")

        current = current.right


print("In-Order:")
dfs_inorder_v1(root)
print()
dfs_inorder_v2(root)
print()
print("------")
# @in-order


# @post-order: 8, 9, 4, 10, 5, 2, 6, 7, 3, 1
def dfs_postorder_v1(node: TreeNode):
    pass


def dfs_postorder_v1(node: TreeNode):
    pass


print("Post-Order:")
dfs_postorder_v1(root)
print()
dfs_postorder_v1(root)
print()
print("------")
# @post-order


# @Level-order: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
def bfs_levelorder(node: TreeNode):
    pass


print("Level-Order:")
dfs_postorder_v1(root)
print()
dfs_postorder_v1(root)
print()
print("------")
# @Level-order
