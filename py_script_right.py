
from typing import List
class Solution:
    #寻找target的右边界
    def right_bound(nums:List[int],target:int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2 
            if nums[mid]  == target:
                #[--ttm----] 为了找右边界。左边就全不要。然后 left = mid+1 
                # 现在的窗口变成 [mid+1,right)
                #来看这个例子。这个情况也就是 直接找到了mid。 并且会在 ----里面进行二分查找。这样会一直触发right = mid 直到 right =left = mid +1
                # 所以最后返回的是 left -1 或者right -1 
                left = mid + 1
            elif nums[mid] < target:
                #[---m-tt-] 说明我们找的 targe 左边不可能出现。一定是在右边。而且右端点也一定是在右边
                # 结果就是 和上面一样 来更新左边
                left = mid + 1
            elif nums[mid] > target:
                #[tt-m---]
                #说明 target 不可能在右边出现。一定是在左边。 而且是左闭右开
                right = mid
            
        return left -1
"""    为什么最后返回 left - 1 而不像左侧边界的函数，返回 left？而且我觉得这里既然是搜索右侧边界，应该返回 right 才对。

答：首先，while 循环的终止条件是 left == right，所以 left 和 right 是一样的，你非要体现右侧的特点，返回 right - 1 好了。

至于为什么要减一，这是搜索右侧边界的一个特殊点，关键在锁定右边界时的这个条件判断："""
                