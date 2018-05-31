import numpy as np

pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
in_order = [4, 7, 2, 1, 5, 3, 8, 6]

# print(pre_order.index(4))

def preTraverse(tree):
    if tree is not None:
        print(tree.val)
        preTraverse(tree.left)
        preTraverse(tree.right)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def reCon(pre, tin, pre_s, pre_e, in_s, in_e):
    if len(pre) == 0:
        return None
    root = TreeNode(pre[pre_s])
    root_index = tin.index(root.val)
    left_num = root_index - in_s
    right_num = in_e - root_index
    if left_num > 0:
        root.left = reCon(pre, tin, pre_s + 1, pre_s + left_num, in_s, root_index - 1)
    if right_num > 0:
        root.right = reCon(pre, tin, pre_s + left_num + 1, pre_e, root_index + 1, in_e)
    return root

tree = reCon(pre_order, in_order, 0, len(pre_order) - 1, 0, len(in_order) - 1)

preTraverse(tree)
