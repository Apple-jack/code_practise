# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def swap(node):
    if node is None:
        return None
    temp = node.left
    node.left = node.right
    node.right = temp
    swap(node.left)
    swap(node.right)
    return node

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is None:
            return None

        return swap(root)
