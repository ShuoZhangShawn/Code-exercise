from typing import Optional

#定义一个节点类
#这个节点类 属性 
#一个是val 表示当前节点的值
#一个是 next 表示当前节点的下一个节点，是一个指针


"""
大概就只有 赋值 更新 维护
三个操作

首先把需要的值 赋值给 p 
然后把 p1 或p2 的指针 更新到下一个节点 那么 这个 p.next的指针就指向了下一个节点
然后更新完了 之后 还要更新 p 的节点

"""


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #先创建一个虚拟头节点
        dummy = ListNode(-1)
        #使用一个指针来指向 虚拟头节点，这个指针主要用来维护合并后的链表的尾部
        p = dummy 
        #使用一个指针来指向 list1 这个指针来维护 list1 的尾部
        p1 = list1 
        #使用一个指针来指向 list2 这个指针来维护 list2 的尾部
        p2 = list2

        #接下来 比较 p1 和p2 的当前节点的大小， 把较小的节点接在 p 的后面。
        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                #是通过把值 赋值给 p.next 的指针来实现吧他们接到一起的。
                p.next = p2
                #移动指针 因为 p2 的第一个元素已经被接到 p 后面了 我们不想重复使用 p2 的第一个元素，因此我们移动 p2 的指针 来将指针指向下一个元素就可以了。
                p2 = p2.next 
            else:
                p.next = p1 
                p1 = p1.next 
            
            #移动 p 的指针
            p = p.next 

        #只要其中一个是空的，那把另外一个接到 p 的后面
        if p1 is not None:
            p.next = p1
        
        if p2 is not None:
            p.next = p2
        #把除了第一个值的节点返回。
        return dummy.next 