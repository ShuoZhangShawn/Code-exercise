#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30201
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #这里使用虚拟头节点。 当我们需要创建虚拟头节点的时候，我们就可以使用虚拟头节点。这样可以免于维护头节点，会比较方便
        #dummy 在这是固定作为新链表的头部的
        dummy = ListNode(-1)
        #这里使用一个指针 来构建/维护 合并后的链表的尾部 
        #我们用指针p 来维护合并后的链表，但是主要还是维护链表的尾部 
        #在l1 l2 中 我们也是会用这个技巧来维护 l1 和 l2 的尾部，这种题目的技巧就是 使用指针来对链表进行维护
        p = dummy 
        p1 = list1
        p2 = list2 

        #下一步我们要把两个链表合并起来。如果两个链表都非空，那么我们比较两个链表的头部，然后选择较小的那个，然后移动指针。
        #如果两个链表中有一个为空，那么我们直接把另一个链表接在后面。
        while p1 is not None and p2 is not None:
            if p1.val < p2.val: #如果 p1的元素比 p2 小的话
                #我们就把 p1 的元素接在 p 的后面
                p.next = p1
                #移动指针，因为 p1 的第一个元素被接到 p 的后面了。我们不想重复使用 p1的元素，这个时候可以通过移动 p1的指针 来将指针指向下一个元素就可以了。
                p1 = p1.next 
            
            else:
                p.next = p2 
                #移动指针
                p2 = p2.next
            
            #移动 p 的 指针
            p = p.next
            #接下来判断两个链表中是否一个有一个是空的。 因为前面我们有一个 while true 的控制循环，因此两个链表中至少有一个是空的。。
            if p1 is not None:
                p.next = p1 

            if p2 is not None:
                p.next = p2 
        #因为 dummy 是虚拟头节点，它的值是-1 不是我们想要的结果。因此我们需要从 dummy 的下一个节点开始返回。也就是说从 dummy.next 也就是 dummy 的下一个节点。
        return dummy.next 

#ACM 格式，我们自己创建函数
#  测试函数
def create_linked_list(arr):
    """根据数组创建链表"""
    if not arr:
        return None
    #仍然使用前面定义的 创建链表的函数
    head = ListNode(arr[0])
    #这次不同的是，我们不是新建一个链表 而是根据数组创建链表。那么这个最初的节点我们就不需要设置为-1 了 而是直接用第一个节点就行了
    current = head
    #定义一个循环，从第二个节点开始，因为第一个节点已经创建了。 这个循环的目的是 创建一个链表，这个链表的每个节点都是根据数组中的元素创建的。
    for i in range(1, len(arr)):
        #创建一个节点。这个节点是 head 的 指针所指向的节点，也就是 数组中 序列为 1 的节点。
        current.next = ListNode(arr[i])
        #移动指针  因为 current在开头的时候是指向 head的指针，然后我们把它指向下一个的指针指向了数组的 第 1 个元素（0-first）。那么这样 自然而然的 current.next 就指向了数组的 第 2 个元素（1-second）。
        current = current.next
    #返回头节点
    return head

def print_linked_list(head):
    """打印链表"""
    #这里是一个打印链表的操作
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1: [1,2,4] 和 [1,3,4]
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print("测试1结果:", print_linked_list(result))  # 应该输出: [1, 1, 2, 3, 4, 4]
    
    # 测试用例2: [] 和 []
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print("测试2结果:", print_linked_list(result))  # 应该输出: []
    
    # 测试用例3: [] 和 [0]
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print("测试3结果:", print_linked_list(result))  # 应该输出: [0]



        
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

