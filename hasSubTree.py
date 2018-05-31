str = 'aabbc'
str1 = 'ab'

i = str.find(str1)

print(i)
preStr = ''

class Solution:
    def __init__(self):
        self.preStr = ''

    def preOrder(self, root):
        if root is None:
            return
        else:
            self.preStr += str(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        self.preStr = ''
        self.preOrder(pRoot1)
        preStr1 = self.preStr

        self.preStr = ''
        self.preOrder(pRoot2)
        preStr2 = self.preStr

        if preStr1.find(preStr2) == -1:
            return False
        else:
            return True