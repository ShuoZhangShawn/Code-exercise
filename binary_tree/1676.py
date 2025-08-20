

#给你输入一棵不含重复值的二叉树，给你输入一个包含若干节点的列表 nodes（这些节点都存在于二叉树中），让你算这些节点的最近公共祖先。
#相对于236题，这次不输入pq两个节点了，而是输出了一个list。
#只需要稍微修改236题的思路，将 是否是某个值的判断 改为是否 集合中是否存在这个val

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        #可以看到 nodes是一个list 而不是两个 val了
        #我们可以用set() 一个集合来把这个list里面的元素全装进去
        #set和dict一样。set是只有key的 dict。确保key不重复
        values = set()
        for node in nodes:
            values.add(node.val)  # 修复：value -> values
        #values是集合
        return self.find(root, values)
    
    def find(self, root: 'TreeNode', values: 'set') -> 'TreeNode':  # 修复：valuse -> values
        #base 如果根节点是None 直接返回None
        if root is None:
            return None
        
        #前序位置
        if root.val in values:
            return root
        
        #遍历左右节点
        left = self.find(root.left, values)  # 修复：添加self.
        right = self.find(root.right, values)  # 修复：添加self.

        #后序位置
        if left is not None and right is not None:
            #当前节点是LCA节点
            return root
        return left if left is not None else right

# ==================== ACM格式代码 ====================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, target_values: set) -> TreeNode:
        return self.find(root, target_values)
    
    def find(self, root: TreeNode, values: set) -> TreeNode:
        #base 如果根节点是None 直接返回None
        if root is None:
            return None
        
        #前序位置
        if root.val in values:
            return root
        
        #遍历左右节点
        left = self.find(root.left, values)
        right = self.find(root.right, values)

        #后序位置
        if left is not None and right is not None:
            #当前节点是LCA节点
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
    k = int(line[1])  # k个目标节点
    
    # 读取目标节点值
    target_values = set()
    for i in range(2, 2 + k):
        target_values.add(int(line[i]))
    
    nodes_info = []
    for _ in range(n):
        val, left, right = map(int, input().split())
        nodes_info.append((val, left, right))
    
    # 构建二叉树
    root = build_tree(nodes_info)
    
    # 查找多个节点的最近公共祖先
    solution = Solution()
    result = solution.lowestCommonAncestor(root, target_values)
    
    # 输出结果
    if result:
        print(result.val)
    else:
        print(-1)

if __name__ == "__main__":
    main()
