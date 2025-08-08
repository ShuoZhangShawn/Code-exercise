#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30201
#
# [209] 长度最小的子数组
#

# @lc code=start
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0 
        right = 0
        
        #关于 windows 的部分 可以维护 window 内的元素和
        windowSum = 0 
        n = len(nums)
        
        while right < n:
            #右边指针会一直向右移动
            #扩张 window 的时机：可以window 可以一直向右扩张
            #如果window大于或者等于 target 的 可以缩小左边的窗口 同时记录结果
            windowSum += nums[right]
            right += 1
            while windowSum >= target and left < right:
                #已经达到target 缩小窗口同时更新答案
                res = min(res, right - left)    
                windowSum -= nums[left]
                left += 1
        return 0 if res == float('inf') else res
        
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

