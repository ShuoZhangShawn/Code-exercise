#
# @lc app=leetcode.cn id=713 lang=python3
# @lcpr version=30201
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #寻找连续子数组的问题。 这个题是滑动窗口的思路
        #经典思路是这样。判断什么时候扩大窗口。判断什么时候缩小窗口。判断什么时候保存结果
        #right 指针从左向右 一直遍历 left指针指向左边的元素。
        #每挪动一次 right指针 判断子数组成绩是否 超过100
        #如果超过100 left 指针向右收缩
        #如果小于100 计数器 +1 
        windowproduct = 1 
        count = 0 
        #初始化计数器
        right = 0
        left = 0
        #初始化 左右指针
        n = len(nums)

        while right < n:
            #这里扩大窗口
            #如果 把 right+=1 放在这里。就会发生 indexError的问题
            #我们直接看最后一次循环
            #假如right的值 是n-1 while 条件 n-1<n 进入循环
            #right +=1执行后 right的值变成了n
            #接下来执行 windowsproduct *= nums[right]
            #right的索引是 n
            #但是 n的 界限是 从0到 n-1 而 nums[n] 就超出了 数组的范围，从而引发了 indexError
            windowproduct *= nums[right]
            right += 1 

            while left <  right and windowproduct >= k:
                #这里缩小窗口
                windowproduct /= nums[left]
                left += 1
                #推出元素
            count += right - left

        #现在 比如 left 到right 是合法子数组
        #但是 不知left 到right。而是 left+1到right  left+2 到right
        #
        return count

        
        
# @lc code=end



#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#

