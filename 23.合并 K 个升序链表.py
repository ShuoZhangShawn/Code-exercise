#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30201
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:   
        #先看看 list 是不是空的 如果是空的，那就返回一个 None 的空结果
        if not lists:
            return None 
        #如果 List 不是空的，那么我们就开始将这些链表合并起来。
        #思路是 先取出 head 节点 然后把 head 节点推到 mini-heap 中
        #下一步从 mini-heap 中取出最小值，然后把这个最小值的节点推到 结果链表中去。
        #接下来把 推出节点的那条 list 的下一个节点推入到 mini-heap 中。这样就能一直去比较同一步的节点的大小。
        dummy = ListNode(-1)
        p = dummy 
        #定义 pq
        pq = []
        
        for i , head in enumerate(lists):
            #这里的 list 里面有多个链表。这的枚举的效果是 把每个 list 都拿出来
            #如果第一个值是空的，那么说明这整个 list 都是空的
            if head is not None:
                #如果不是空的，那把第一个值压入到 pq 这个最小堆中
                # head.val 和i 是给 pq 这个最小堆用来排序的。
                #如果我重载了运算符，就可以在 Python 中用 < 来比较两个 ListNode 对象
                #heapq.heappush(pq, head)
                heapq.heappush(pq,(head.val,i,head))
                
        while pq:
            #从 pq 中取出最小值，并且压入 我们的 dummy list
            #这里把它取出来
            val, i , node = heapq.heappop(pq)
            #这里把它压进去
            p.next = node 
            #因为我们把其中一个链表的元素压进去了一个，为了让这个链表的其他元素也能进入二叉堆来参与比大小，我们得把 我们刚才定义的 node 节点的下一个节点弄进去。
            if node.next is not None:
                heapq.heappush(pq,(node.next.val,i,node.next))
            #完成了这些操作，我们应该把 p 的指针移向后面一位，因为我们已经给当前位置赋值了。
            p = p.next
        
        return dummy.next
        
# @lc code=end

# ===== ACM 格式代码 =====

def create_linked_list(arr):
    """根据数组创建链表"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def linked_list_to_array(head):
    """将链表转换为数组用于输出"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def main():
    """ACM 格式的主函数"""
    import sys
    
    # 读取输入
    line = input().strip()
    
    # 处理空输入的情况
    if line == "[]":
        print("[]")
        return
    
    # 解析输入格式：[[1,4,5],[1,3,4],[2,6]]
    line = line.replace('[', '').replace(']', '')
    if not line:
        print("[]")
        return
        
    # 分割各个链表
    lists_str = line.split(',')
    
    # 构建链表数组
    lists = []
    current_list = []
    
    i = 0
    while i < len(lists_str):
        val_str = lists_str[i].strip()
        if val_str:  # 非空值
            current_list.append(int(val_str))
        
        # 检查是否是一个链表的结束（简单处理）
        # 这里假设输入格式是标准的，每三个数字为一组
        if len(current_list) > 0 and (i + 1) % 3 == 0:
            lists.append(create_linked_list(current_list))
            current_list = []
        i += 1
    
    # 处理最后一个链表
    if current_list:
        lists.append(create_linked_list(current_list))
    
    # 创建 Solution 实例并解决问题
    solution = Solution()
    result = solution.mergeKLists(lists)
    
    # 输出结果
    result_array = linked_list_to_array(result)
    print(str(result_array).replace(' ', ''))

# 测试函数
def test():
    """测试函数"""
    print("=== 测试用例 ===")
    
    # 测试用例 1: [[1,4,5],[1,3,4],[2,6]]
    lists1 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    solution = Solution()
    result1 = solution.mergeKLists(lists1)
    print("测试用例 1:", linked_list_to_array(result1))  # 期望: [1,1,2,3,4,4,5,6]
    
    # 测试用例 2: []
    lists2 = []
    result2 = solution.mergeKLists(lists2)
    print("测试用例 2:", linked_list_to_array(result2) if result2 else [])  # 期望: []
    
    # 测试用例 3: [[]]
    lists3 = [None]
    result3 = solution.mergeKLists(lists3)
    print("测试用例 3:", linked_list_to_array(result3) if result3 else [])  # 期望: []

if __name__ == "__main__":
    # 如果要运行测试，取消下面这行的注释
    test()
    
    # ACM 格式输入输出（注释掉测试函数后使用）
    # main()


