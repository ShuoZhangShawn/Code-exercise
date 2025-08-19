# ACM格式测试用例
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 定义：在以 root 为根的二叉树中寻找值为 val 的节点
def find(root: TreeNode, val: int) -> TreeNode:
    # base case
    if not root:
        return None
    # 看看 root.val 是不是要找的
    if root.val == val:
        return root
    # root 不是目标节点，那就去左子树找
    left = find(root.left, val)
    if left:
        return left
    # 左子树找不着，那就去右子树找
    right = find(root.right, val)
    if right:
        return right
    # 实在找不到了
    return None

def build_tree(nodes):
    # nodes: list of (val, left_idx, right_idx), -1 means None
    tree = [TreeNode(val) for val, _, _ in nodes]
    for idx, (val, l, r) in enumerate(nodes):
        tree[idx].left = tree[l] if l != -1 else None
        tree[idx].right = tree[r] if r != -1 else None
    return tree[0] if tree else None

def _run_from_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    _run_from_lines(lines)


def _run_from_lines(lines):
    it = iter(lines)
    n, target = map(int, next(it).split())
    nodes = [tuple(map(int, next(it).split())) for _ in range(n)]
    root = build_tree(nodes)
    res = find(root, target)
    print(res.val if res else "None")


if __name__ == "__main__":
    # 用法：
    # 1) python find_a_ele.py input.txt   （从文件读取）
    # 2) python find_a_ele.py < input.txt （ACM：从标准输入读取）
    import sys
    if len(sys.argv) >= 2:
        _run_from_file(sys.argv[1])
    elif not sys.stdin.isatty():
        lines = [line.strip() for line in sys.stdin if line.strip()]
        _run_from_lines(lines)
    else:
        print("usage: python find_a_ele.py <input.txt>  or  python find_a_ele.py input.txt", file=sys.stderr)
        sys.exit(1)