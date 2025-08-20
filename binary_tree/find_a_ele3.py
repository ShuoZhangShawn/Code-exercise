from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right



#The efficiency will be decreasing, because this method will traverse each node of the tree
def find(root:TreeNode,val:int) -> TreeNode:
    if root is None:
        return None
    #try to find the outcome in left and right tree
    left = find(root.left,val)
    right = find(root.right,val)
    
    #backend position.check whether the Root is target
    if root.val == val:
        return root
    
    return left if left is not None else right

def build_tree(nodes: list[tuple[int, int, int]]) -> Optional[TreeNode]:
    # nodes: list of (val, left_idx, right_idx), -1 means None
    if not nodes:
        return None
    tree = [TreeNode(val) for val, _, _ in nodes]
    for idx, (val, l, r) in enumerate(nodes):
        tree[idx].left = tree[l] if l != -1 else None
        tree[idx].right = tree[r] if r != -1 else None
    return tree[0]

def _run_from_lines(lines: list[str]) -> None:
    it = iter(lines)
    n, target = map(int, next(it).split())
    nodes: list[tuple[int, int, int]] = [tuple(map(int, next(it).split())) for _ in range(n)]
    root = build_tree(nodes)
    res = find(root, target)
    print(res.val if res else "None")


def _run_from_file(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    _run_from_lines(lines)


if __name__ == "__main__":
    # 用法：
    # 1) python find_a_ele2.py input.txt   （从文件读取）
    # 2) python find_a_ele2.py < input.txt （从标准输入读取）
    import sys
    if len(sys.argv) >= 2:
        _run_from_file(sys.argv[1])
    elif not sys.stdin.isatty():
        lines = [line.strip() for line in sys.stdin if line.strip()]
        _run_from_lines(lines)
    else:
        print("usage: python find_a_ele2.py <input.txt>  or  python find_a_ele2.py input.txt", file=sys.stderr)
        sys.exit(1)