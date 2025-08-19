#给你输入一棵没有重复元素的二叉树根节点 root 和一个目标值 val，请你写一个函数寻找树中值为 val 的节点。
from typing import Optional
def find(root: TreeNode, val: int) -> TreeNode:
    #base case
    if not root:
        return None
    #check whether the root node is target
    if root.val == val:
        return root
    #root not the target, go to check the left tree
    left = find(root.left,val)
    if left:
        return left
    
    # if not left, check the right
    right = find(root.right.val)
    if right:
        return right
    
    #if we find nothing
    return None
    