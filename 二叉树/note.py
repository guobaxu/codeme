# 快速排序是二叉树的前序遍历
# 归并排序是二叉树的后序遍历

# 快速排序
def quicksort(nums:list[int], left:int, right:int):
    #### 前序位置 ####
    # 通过交换元素构造/寻找分界点，partition实现功能
    p = partition(nums, left, right)

    # 左边子数组
    quicksort(nums, left, p-1)
    # 右边子数组
    quicksort(nums, p+1, right)

# 归并排序
def mergesort(nums:list[int], left:int, right:int):
    mid = (left+right) // 2
    # 左边子数组
    mergesort(nums, left, mid)
    # 右边子数组
    mergesort(nums, mid+1, right)

    #### 后序位置 ####
    # 合并子数组
    merge(nums, left, mid, right)

# 二叉树遍历框架（递归形式）
# traverse 函数作用就是便利二叉树所有节点
def traverse(root):
    if root is None:
        return
    # 前序位置
    traverse(root.left)
    # 中序位置
    traverse(root.right)
    # 后序位置

"""
前中后序是遍历二叉树过程中处理每一个节点的三个特殊时间点
1.前序位置的代码在刚刚进入一个二叉树节点的时候执行
2.后序位置的代码在将要离开一个二叉树节点的时候执行
3.中序位置的代码在一个二叉树节点左子树都遍历完，即将开始遍历右子树的时候执行

二叉树的所有问题，就是让你在前中后序位置注入巧妙的代码逻辑，去达到自己的目的
只需要单独思考每一个节点应该做什么，其他的不用你管，抛给二叉树遍历框架，递归会在所有节点上做相同的操作

二叉树解题的思维模式
【遍历】
1.是否可以通过遍历一遍二叉树得到答案
2.如果可以，用一个traverse函数配合外部变量实现
【递归】
1.是否可以通过子问题（子树）的答案推导出原问题的答案?
2.如果可以，定义一个递归函数，写出这个递归函数的定义，并充分利用这个函数的返回值
思考：
如果单独抽出一个二叉树节点，它需要做什么事情？需要在什么时候（前/中/后序位置）做？
其他的节点不用你操心，递归函数会帮你在所有节点上执行相同的操作。
"""

