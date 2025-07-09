#
# @lc app=leetcode.cn id=1658 lang=python3
# @lcpr version=30201
#
# [1658] 将 x 减到 0 的最小操作数
#

# @lc code=start
from typing import List
#这个是滑动窗口的问题

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        #先写模板
        #要求找到 x恰好减到0 所需要的最少操作数
        #这是一个二维数组，并且每次只能操作最左边或最右边的元素
        #这就可以用双指针，左右指针
        #可以使用模板中的哈希表 一个 window 记录当前情况。一个need 记录需求
        #need = {}
        #windows = {}
        #但是问题来了。need 的要求是两个元素的合为 x。 这就不知道怎么做了。 现在去看一下东哥的解法。
        #首先东哥介绍了暴力写法。我可以选择移除最左边或者最右边的元素，然后对剩下的元素进行递归调用操作，直到x减少到0
        #题目让我们删除掉边缘和为x的数组。 如果我们做到了。那剩下来的东西就是 nums的一个子数组。这就把问题转换成了一个寻找子数组的问题
        #目的是返回最少操作数。也就是说让我们尽可能地少去减少元素。也就是寻找最长的子数组
        #也就是说 我们要寻找nums中 元素和为 sum(nums) -x 的最长子数组
        #这是典型的逆向思维。我们不找和为k的。而是找到把k
        #这样我们就把这个问题转换为了一个 滑动窗口的问题。
        n = len(nums)
        target = sum(nums) - x

        left = 0
        right = 0


        #记录窗口内所有元素之和
        window_sum = 0
        #记录目标子数组的最大长度
        max_len = float('-inf')
        #目的是 寻找到 当值为sum(nums)-x 时，最长的连续子数组




        #初始化两个指针
        #我们是怎么找到符合条件的子数组的呢。就是通过window
        #接下来要考虑的是 什么时候扩大窗口。什么时候缩小窗口。什么时候得到答案
        
        #当窗口元素小于 target的时候 扩大窗口 但是一般情况下 right指针是一直向右走的。
        #当窗口元素大于 target的时候 缩小窗口
        #当窗口元素 等于 target的时候 得到答案
  
        while right < n:
            #把右指针的元素加入到窗口元素中
            window_sum += nums[right]
            right += 1



            while window_sum > target and left < right:
                #当窗口元素超过了target的时候 收缩左边的窗口
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                max_len = max(max_len, right - left)

            #当窗口元素等于 target的时候 得到答案。这个答案是通过 max_len 这个变量来维护的

        return -1 if max_len == float('-inf') else n - max_len



        
# @lc code=end



#
# @lcpr case=start
# [1,1,4,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5,6,7,8,9]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,20,1,1,3]\n10\n
# @lcpr case=end

#

