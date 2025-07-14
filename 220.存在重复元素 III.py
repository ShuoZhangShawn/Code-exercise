#
# @lc app=leetcode.cn id=220 lang=python3
# @lcpr version=30201
#
# [220] 存在重复元素 III
#

# @lc code=start
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        from sortedcontainers import SortedList
        window  = SortedList()
        #这个包会让 插入的所有元素都自动排序
        for i in range(len(nums)):
            # 为了防止 i == j，所以在扩大窗口之前先判断是否有符合题意的索引对 (i, j)
            # 查找略大于 nums[i] 的那个元素
            pos = window.bisect_left(nums[i])
            # 这是把 nums[i] 在 sortedList 中的位置拿到了。
            # 但是这个位置是 属于 nums[i] 这个值 的后面一位置的数字的。 也就是说 window[pos] 是大于等于 nums[i]的
            #这个方法会把 当前的值给一个位置。比如 nums[i] = 6。 window为 [1,3,5,7] 那么 window[pos] = 3  就是在 5和7中间
            #但是现在 window[pos] 也是就 window[3] 的value 是7。 因此 window[pos] 是 距离nums[i] 最近的一个value
            #如果这个 value 和 nums[i]的差 大于t 。也就是说在排好序的情况下，就没有比这个值更合适的。因此就没有合适的值 让他俩的差小于t
            #所以这样可以写判断


            if pos < len(window) and window[pos] - nums[i] <= valueDiff:
            # 查找离 nums[i] 最近的两个元素：一个是大于或等于 nums[i] 的最小元素（window[pos]），
            # 另一个是小于或等于 nums[i] 的最大元素（window[pos - 1]）。
            # 如果这两个元素之间的差值都不满足 t，那么没有其他元素会符合条件。
                return True
            if pos > 0 and nums[i] - window[pos -1] <= valueDiff:
                #同理。我们也可以知道 window[pos -1] 就是 比 nums[i] 小 但是相邻的 值。
                return True
            #
            #扩大窗口
            window.add(nums[i])

            #如果太长 超过了k 缩小
            if len(window) > indexDiff:
                window.remove(nums[i - indexDiff])
        return False


"""
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        from sortedcontainers import SortedList
        window = SortedList()
        
        # SortedList 自动保持元素的有序性
        for i in range(len(nums)):
            # 查找离 nums[i] 最近的两个元素
            pos = window.bisect_left(nums[i])
            # pos 是 `nums[i]` 应该插入的位置
            # 如果 `pos` 位置上的元素大于或等于 `nums[i]`，检查它们的差值是否小于等于 valueDiff
            if pos < len(window) and window[pos] - nums[i] <= valueDiff:
                return True
            
            # 如果 `pos - 1` 是小于 `nums[i]` 的最大元素，检查它们的差值是否小于等于 valueDiff
            if pos > 0 and nums[i] - window[pos - 1] <= valueDiff:
                return True

            # 扩大窗口，加入当前元素
            window.add(nums[i])

            # 如果窗口大小超过了 indexDiff，移除最旧的元素
            if len(window) > indexDiff:
                window.remove(nums[i - indexDiff])

        return False

"""

            
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,5,9,1,5,9]\n2\n3\n
# @lcpr case=end

#

