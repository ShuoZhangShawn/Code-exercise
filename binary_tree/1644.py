from typing import Optional

class TreeNode:
	def __init__(self, val: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def __init__(self):
		# 用于记录 p 和 q 是否存在于二叉树中
		self.foundP = False
		self.foundQ = False

	def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "Optional[TreeNode]":
        
		res = self.find(root, p.val, q.val)
		if not self.foundP or not self.foundQ:
			return None
		# p 和 q 都存在二叉树中，才有公共祖先
		return res

	# 在二叉树中寻找 val1 和 val2 的最近公共祖先节点
	def find(self, root: "Optional[TreeNode]", val1: int, val2: int) -> "Optional[TreeNode]":
		if not root:
			return None
		left = self.find(root.left, val1, val2)
		right = self.find(root.right, val1, val2)

		# 后序位置，判断当前节点是不是 LCA 节点
		if left and right:
			return root

		# 后序位置，判断当前节点是不是目标值
		if root.val == val1 or root.val == val2:
			# 找到了，记录一下
			if root.val == val1:
				self.foundP = True
			if root.val == val2:
				self.foundQ = True
			return root

		return left if left else right
            


def build_tree(nodes: "list[tuple[int, int, int]]") -> "Optional[TreeNode]":
	"""根据 (val, left_idx, right_idx) 列表构造二叉树，根约定为索引 0。-1 表示 None。"""
	if not nodes:
		return None
	tree = [TreeNode(val) for val, _, _ in nodes]
    #创建所有节点对象
    ## 结果：
     
    #tree = [
    #    TreeNode(3),  # tree[0]
    #    TreeNode(1),  # tree[1] 
    #    TreeNode(5)   # tree[2]
    #    此时所有节点都是孤立的，没有连接：
    #]
    
    #建立父子连接关系
	for idx, (val, l, r) in enumerate(nodes):
		tree[idx].left = tree[l] if l != -1 else None
        #给left right 指针赋值
		tree[idx].right = tree[r] if r != -1 else None
	return tree[0]
    #return tree[0] 根节点 整棵树的入口



    # 不够优雅的方式
    #lines = ["3 5 1", "3 1 2", "1 -1 -1", "5 -1 -1"]
    #idx = 0

    # 读第一行
    #n, p_val, q_val = map(int, lines[idx].split())
    #idx += 1

    # 读接下来的 n 行
    #for i in range(n):
    #    node_info = lines[idx]
    #    idx += 1
    #    # 处理...
def _run_from_lines(lines: "list[str]") -> None:
    # 第一行：n p q
    n, p_val, q_val = map(int, lines[0].split())
    
    # 后续 n 行：val left_idx right_idx
    nodes = []
    for i in range(1, n + 1):  # 从第2行开始，读n行
        val, left_idx, right_idx = map(int, lines[i].split()) # 映射：str -> int
        #可迭代对象的每个元素应用同一个函数。
        nodes.append((val, left_idx, right_idx))
    
    # 或者更简洁的列表推导式
    # nodes = [tuple(map(int, lines[i].split())) for i in range(1, n + 1)]
    #循环中是先解包 然后重新打包
    #tuple是直接转换 不解包 但是不懂解包和不解包的区别
    
    """
    # 例子1：手动解包版本
    def method1():
        line = "3 1 2"
        nums = map(int, line.split())     # nums 是 map 对象
        a, b, c = nums                    # 👈 解包：把 map 对象分解成 3 个变量
        return (a, b, c)                  # 👈 重新打包：用 3 个变量构造元组

    # 例子2：直接转换版本  
    def method2():
        line = "3 1 2"
        nums = map(int, line.split())     # nums 是 map 对象
        return tuple(nums)                # 👈 直接转换：map 对象 -> 元组，没有中间变量
        
        把nums
        从[3,1,2]
        转换为(3,1,2)

    print(method1())  # (3, 1, 2)
    print(method2())  # (3, 1, 2)
    nodes = [
        (3, 1, 2),    # 第一个元组
        (1, -1, -1),  # 第二个元组  
        (5, -1, -1)   # 第三个元组
    ]
    列表嵌套元组
    """
    
    
    # 重要：构建二叉树！
    root = build_tree(nodes)
    
    # 创建查找目标节点
    p = TreeNode(p_val)
    q = TreeNode(q_val)

    # 执行算法
    sol = Solution()
    ans = sol.lowestCommonAncestor(root, p, q)
    print(ans.val if ans else "None")

"""
迭代器的方式
def _run_from_lines(lines: "list[str]") -> None:
	it = iter(lines)
    #创建迭代器
    # 迭代器有"状态"，记住当前位置. print(next(it)) 一直执行的话，最后会报错 StopIteration
    #如果不用迭代器 还得手动管理索引
    
	# 第一行：n p q。 先读取第一行
	n, p_val, q_val = map(int, next(it).split())
	# 后续 n 行：val left_idx right_idx
	nodes: "list[tuple[int, int, int]]" = [tuple(map(int, next(it).split())) for _ in range(n)]
	root = build_tree(nodes)
 

	# 你的核心接口接收 TreeNode，因此这里用值构造占位节点（内部按 val 寻找）
	p = TreeNode(p_val)
	q = TreeNode(q_val)

	sol = Solution()
	ans = sol.lowestCommonAncestor(root, p, q)
	print(ans.val if ans else "None")
 """


def _run_from_file(path: str) -> None:
	with open(path, "r", encoding="utf-8") as f:
		lines = [line.strip() for line in f if line.strip()]
	_run_from_lines(lines)


if __name__ == "__main__":
	# 用法：
	# 1) python 1644.py 1644.txt   （从文件读取）
	# 2) python 1644.py < 1644.txt （从标准输入读取）
	import sys
	if len(sys.argv) >= 2:
        #方式1传文件路径参数
		_run_from_file(sys.argv[1])
	elif not sys.stdin.isatty():
        #方式2标准输入重定向
        #我们的操作是 python 1644.py < 1644.txt Shell（你的终端）会把文件内容"接管
        #程序以为还是从键盘读，实际上读的是文件内容
        #相当于
        #with open("1644.txt", "r") as f:
            #lines = [line.strip() for line in f if line.strip()]
		lines = [line.strip() for line in sys.stdin if line.strip()]
        #.strip()是字符串方法，用来去掉首位的空白字符。
        #sys.stdin是一整个文件，重定向的时候指向这个文件了。它是一个可遍历的文件。line是一行
		_run_from_lines(lines)
	else:
        #啥都没有，提示用法
		print("usage: python 1644.py <1644.txt>  or  python 1644.py 1644.txt", file=sys.stderr)
		sys.exit(1)
