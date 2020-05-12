# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    # Добавление узла
    def insert(self, data):
        if self.val == data:
            return False

        elif self.val > data:
            if self.left:
               return self.left.insert(data)
            else:
                self.left = TreeNode(data)
                return True

        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = TreeNode(data)
            return True
# Определение бинарного дерева
class Tree:
    def __init__(self):
        self.root = None
    # Добавление элемента в бинарное дерево
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = TreeNode(data)
            return True
    # Отрисовка бинарного дерева
    def drawtree(root):
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1

        def jumpto(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

        def draw(node, x, y, dx):
            if node:
                t.goto(x, y)
                jumpto(x, y - 20)
                t.write(node.val, align='center', font=('Arial', 12, 'normal'))
                draw(node.left, x - dx, y - 60, dx / 2)
                jumpto(x, y - 20)
                draw(node.right, x + dx, y - 60, dx / 2)

        import turtle
        t = turtle.Turtle()
        t.speed(0);
        turtle.delay(0)
        h = height(root)
        jumpto(0, 30 * h)
        draw(root, 0, 30 * h, 40 * h)
        t.hideturtle()
        turtle.mainloop()

class Solution(object):

    def collect(self, root, result):
        if root == None:
            return None
        Solution.collect(self,root.left,result)
        result.append(root.val)
        Solution.collect(self,root.right,result)
        return result

    def getMinimumDifference(self, root):
        if root == None:
            return None
        leaves = []
        leaves = Solution.collect(self, root,leaves)

        minval = abs(leaves[0] - leaves[1])
        for i in range(0,len(leaves) - 1):
            if abs(leaves[i] - leaves[i+1]) < minval:
                minval = abs(leaves[i] - leaves[i+1])

        return minval


# -----------------------------------------
# Заполнение бинарного дерева списком elems
elems1 = [1,3,2]
# elems2 = [2,1,3,4,7]
T = Tree()
T2 = Tree()
for i in range(0,len(elems1)):
    T.insert(elems1[i])
# for i in range(0,len(elems2)):
#     T2.insert(elems2[i])
# -----------------------------------------
# Отрисовка дерева
# Tree.drawtree(T.root)
# -----------------------------------------


# Tree.drawtree(Solution.getMinimumDifference(0,[0,1,2,3,4,5]))
# [0,1,2,3,4,5]
print(Solution.getMinimumDifference(0,T.root))