# 定义树节点结构
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
二叉树最大深度
'''
maxdepth = 0
# 当前的深度
depth = 0

def MaxDepth(root:TreeNode)->int:
    traverse(root)
    return maxdepth

def traverse(root:TreeNode)->None:
    # 边界条件
    if not root:
        return

    # 前序位置：当前深度
    depth += 1
    if not root.left and not root.right:
        # 叶子节点
        maxdepth = max(maxdepth, depth)
    # 左子树
    traverse(root.left)
    # 右子树
    traverse(root.right)
    # 后序位置
    depth -= 1

# 递归解法
# 函数定义：输入根节点，返回这颗二叉树的最大深度
def MaxDepth_recursion(root:TreeNode)->int:
    # 边界条件
    if not root:
        return 0
    # 利用定义，计算左右子树的最大深度
    leftdepth = MaxDepth_recursion(root.left)
    rightdepth = MaxDepth_recursion(root.right)
    # 加上根节点自己的高度
    return max(leftdepth, rightdepth) + 1

'''
力扣543题：二叉树的直径
'''
# 递归解法
class MaxDiameter:
    def __init__(self) -> None:
        self.maxd = 0
    
    def diameterOFbinarytree(self, root:TreeNode) -> int:
        self.traverse(root)
        return self.maxd
    
    # 遍历二叉树
    # 函数定义：输入根节点，返回当前节点二叉树的最大直径（左右子树的最大深度之和）
    def traverse(self) -> None:
        # 边界条件
        if not root:
            return
        
        # 对每个节点计算直径
        leftMax = self.MaxDepth_recursion(root.left)
        rightMax = self.MaxDepth_recursion(root.right)
        current_maxd = leftMax + rightMax

        # 更新全局最大直径
        self.maxd = max(self.maxd, current_maxd)

        self.traverse(root.left)
        self.traverse(root.right)

        return

    # 返回当前节点二叉树的最大深度
    def MaxDepth_recursion(self, root:TreeNode) -> int:
        # 边界条件
        if not root:
            return 0
        # 利用定义，计算左右子树的最大深度
        leftdepth = MaxDepth_recursion(root.left)
        rightdepth = MaxDepth_recursion(root.right)
        # 加上根节点自己的高度
        return max(leftdepth, rightdepth) + 1
    
# 解法2
class MaxDiameterSolution2:
    def __init__(self):
        # 记录最大直径的长度
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxDepth(root)
        return self.maxDiameter

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        # 后序位置，顺便计算最大直径
        myDiameter = leftMax + rightMax
        self.maxDiameter = max(self.maxDiameter, myDiameter)

        return 1 + max(leftMax, rightMax)
