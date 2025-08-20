import os
import sys

def _run_from_lines(lines: list[str]) -> int:
    # 建议在这行打断点：进入函数看 locals 里的 lines
    total = 0
    for i, line in enumerate(lines):
        n = int(line.strip())
        total += n
        if n < 0:
            # 这里演示条件断点：当 n < 0 时停下
            pass
    return total

def parse_from_stdin() -> list[str]:
    # 建议在下面两行打断点：查看逐行读取的效果
    lines = []
    for _ in range(3):
        lines.append(sys.stdin.readline())
    return lines

def main():
    # ① 从命令行参数读一个文件路径（可选）
    txt_path = sys.argv[1] if len(sys.argv) > 1 else None

    # ② 读取三行数据：优先从文件，其次从标准输入（ACM风格）
    if txt_path and os.path.exists(txt_path):
        with open(txt_path) as f:
            lines = f.readlines()
    else:
        lines = parse_from_stdin()

    # ③ 调用核心逻辑（建议在这一行设置 Step Into）
    ans = _run_from_lines(lines)

    # ④ 看看结果（在这行打个断点，验证 ans）
    print("ANS =", ans)

if __name__ == "__main__":
    main()
