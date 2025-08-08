#
# @lc app=leetcode.cn id=875 lang=python3
# @lcpr version=30201
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
from typing import List
class Solution:
    # 定义：速度为 x 时，需要 f(x) 小时吃完所有香蕉
    # f(x) 随着 x 的增加单调递减
    def f(self,piles:List[int],x:int) -> int:
        hours = 0
        for i in range(len(piles)):
            hours += piles[i] // x
            if piles[i] % x != 0:
                hours += 1
        return hours
    #吃香蕉的速度越快，所需的时间越短。
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #我们的目的就是。在x的取值范围内。
    #寻找一个 最小的 x因为珂珂想慢点吃。
    #但是同时 要在时间H的约束内 吃掉所有香蕉。
    #f是单调递减的函数。
    # 所以珂珂吃香蕉这个题目 是一个搜索左侧边界的二分搜索算法
        left = 1
        right = 1000000000+1
        while left < right:
            mid = left + (right - left) // 2
            if self.f(piles,mid) == h:
                right = mid
                  #我们的目的是 搜索左侧边界
                  #当有值满足要求的时候，我们要向左搜索。
            elif self.f(piles,mid) > h:
                  left = mid + 1
            elif self.f(piles,mid) < h:
                  right = mid
        return left

        
        
# @lc code=end



#
# @lcpr case=start
# [3,6,7,11]\n8\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n5\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n6\n
# @lcpr case=end

#

