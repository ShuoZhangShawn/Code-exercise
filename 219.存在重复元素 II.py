#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30201
#
# [219] 存在重复元素 II
#

# @lc code=start
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #滑动窗口问题
        #当窗口大小小于 k 的时候 扩大窗口。索引从 0 到 k-1。 需要判断的是 k 个元素 而不是k 个索引
        #当窗口大小大于 k 的时候 缩小窗口
        #当窗口大小等于 k 且窗口中 有重复元素 返回 true

        #set() 是一个集合类型
        #set 是一个无序、去重、快速查找的容器**，内部不能有重复元素。

        left = 0
        right = 0
        window = set()
        n = len(nums)
        #初始化
        #数组索引是 0 到 n-1 
        while right < n:
            #right 最多走到 len(nums) -1
            if nums(right) in window:
                return True
            window.add(nums[right])
            right += 1

            if right - left > k:
                window.remove(nums[left])
                left += 1 
        
        return False
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#

