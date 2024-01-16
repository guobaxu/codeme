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
