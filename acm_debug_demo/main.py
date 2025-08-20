import sys, os

# 让 ACM 代码仍然用 input()，但支持传一个 txt 路径来当 stdin（便于调试器）
if len(sys.argv) > 1:
    sys.stdin = open(sys.argv[1], "r", encoding="utf-8")

def parse_stdin():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    return n, arr

def find_first_even(arr):
    for x in arr:
        if x % 2 == 0:       # ← 适合打条件断点的位置
            return x
    return None

def main():
    n, arr = parse_stdin()   # ← 在这里打断点可“单步进入”函数
    even = find_first_even(arr)
    if even is None:
        print("no even")
    else:
        print(even)

if __name__ == "__main__":
    main()
