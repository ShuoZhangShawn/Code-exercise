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
        

        left = find(root.left,val1,val2)
        right = find(root.right,val1,val2)
        #后序位置，已经知道左右子树是否存在目标值
        #当左右都没有的时候 直接返回root
        if left is not None and right is not None:
            #当前节点是LCA节点
            #记录下来
            #+++++
            self.lca = root
            #+++++
            return root

        return left if left left is not None else right

        
        
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

