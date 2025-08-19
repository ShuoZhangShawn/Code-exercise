#现在要写一个新的函数不在找值为val的节点 而是找到 val1 或者val2 的节点
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find(root: TreeNode, val1: int, val2: int) -> TreeNode:
    #base case
    if root is None:
        return None

    if root.val == val1 or root.val == val2:
        return root
    
    #左右子树寻找
    left = find(root.left, val1, val2)
    right = find(root.right, val1, val2)
    
    return left if left is not None else right

def build_tree(nodes_info):
    """根据节点信息构建二叉树"""
    if not nodes_info:
        return None
    
    # 创建所有节点
    nodes = {}
    for val, left_val, right_val in nodes_info:
        if val not in nodes:
            nodes[val] = TreeNode(val)
    
    # 建立父子关系
    root = None
    children = set()
    
    for val, left_val, right_val in nodes_info:
        node = nodes[val]
        
        # 设置左孩子
        if left_val != -1:
            if left_val not in nodes:
                nodes[left_val] = TreeNode(left_val)
            node.left = nodes[left_val]
            children.add(left_val)
        
        # 设置右孩子
        if right_val != -1:
            if right_val not in nodes:
                nodes[right_val] = TreeNode(right_val)
            node.right = nodes[right_val]
            children.add(right_val)
    
    # 找到根节点（不是任何节点的孩子）
    for val, _, _ in nodes_info:
        if val not in children:
            root = nodes[val]
            break
    
    return root

def main():
    # 读取输入
    line = input().split()
    n = int(line[0])
    val1 = int(line[1])
    val2 = int(line[2])
    
    nodes_info = []
    for _ in range(n):
        val, left, right = map(int, input().split())
        nodes_info.append((val, left, right))
    
    # 构建二叉树
    root = build_tree(nodes_info)
    
    # 查找节点
    result = find(root, val1, val2)
    
    # 输出结果
    if result:
        print(result.val)
    else:
        print(-1)

if __name__ == "__main__":
    main()
    
