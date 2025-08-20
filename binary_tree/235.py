# LeetCode 235: 二叉搜索树的最近公共祖先
# 不含重复值的二叉搜索树，存在于树中的两个节点p和q，请计算p和q的最近公共祖先节点

from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 保证val1 <= val2
        val1 = min(p.val, q.val)
        val2 = max(p.val, q.val)
        return self.find(root, val1, val2)
    
    def find(self, root: 'TreeNode', val1: int, val2: int) -> 'TreeNode':
        if root is None:
            return None
        if root.val > val2:
            # 当前节点太大，去左子树找
            return self.find(root.left, val1, val2)
        if root.val < val1:
            # 当前节点太小，去右子树找
            return self.find(root.right, val1, val2)
        # val1 <= root.val <= val2，当前节点就是LCA
        return root


# ACM 格式 - 简洁且便于调试
def main():
    # 读取输入：n p_val q_val
    n, p_val, q_val = map(int, input().split())
    
    # 读取节点信息并构建BST
    nodes = []
    for _ in range(n):
        val, left_idx, right_idx = map(int, input().split())
        nodes.append((val, left_idx, right_idx))
    
    # 构建二叉树
    tree = [TreeNode(val) for val, _, _ in nodes]
    for idx, (val, l, r) in enumerate(nodes):
        tree[idx].left = tree[l] if l != -1 else None
        tree[idx].right = tree[r] if r != -1 else None
    
    # 创建目标节点并执行算法
    p = TreeNode(p_val)
    q = TreeNode(q_val)
    sol = Solution()
    ans = sol.lowestCommonAncestor(tree[0], p, q)
    
    # 输出结果
    print(ans.val if ans else "None")

if __name__ == "__main__":
    main()