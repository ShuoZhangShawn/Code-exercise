#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30202
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #最后加的辅助变量
    # 用一个外部变量来记录是否已经找到 LCA 节点
    def __init__(self):
        self.lca = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root,p.val,q.val)
    
    #在二叉树中寻找val1和val2的最近公共祖先节点
    def find(self,root:'TreeNode',val1:int,val2:int)-> 'TreeNode' :
        if root is None:
            return None
        #++++
        if self.lca is not None:
            return None
        #++++
        #if traverse the target return the outcome
        if root.val ==val1 or root.val == val2:
            #find the target return the outcome
            return root
        

        left = self.find(root.left,val1,val2)
        right = self.find(root.right,val1,val2)
        #后序位置，已经知道左右子树是否存在目标值
        #当左右都没有的时候 直接返回root
        if left is not None and right is not None:
            #当前节点是LCA节点
            #记录下来
            #+++++
            self.lca = root
            #+++++
            return root

        return left if left is not None else right

        
        
# @lc code=end



#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n2\n
# @lcpr case=end

#

# ==================== ACM格式代码 ====================

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #最后加的辅助变量
    # 用一个外部变量来记录是否已经找到 LCA 节点
    def __init__(self):
        self.lca = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None  # 重置lca
        return self.find(root, p.val, q.val)
    
    #在二叉树中寻找val1和val2的最近公共祖先节点
    def find(self, root: 'TreeNode', val1: int, val2: int) -> 'TreeNode':
        if root is None:
            return None
        #++++
        if self.lca is not None:
            return None
        #++++
        #if traverse the target return the outcome
        if root.val == val1 or root.val == val2:
            #find the target return the outcome
            return root
        
        left = self.find(root.left, val1, val2)
        right = self.find(root.right, val1, val2)
        #后序位置，已经知道左右子树是否存在目标值
        #当左右都没有的时候 直接返回root
        if left is not None and right is not None:
            #当前节点是LCA节点
            #记录下来
            #+++++
            self.lca = root
            #+++++
            return root

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
    
    # 查找最近公共祖先
    solution = Solution()
    p = TreeNode(val1)
    q = TreeNode(val2)
    result = solution.lowestCommonAncestor(root, p, q)
    
    # 输出结果
    if result:
        print(result.val)
    else:
        print(-1)

if __name__ == "__main__":
    main()

