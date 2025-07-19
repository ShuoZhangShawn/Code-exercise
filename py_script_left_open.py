
from typing import List
#寻找左侧边界的二分搜索
class Soultion:
    def left_bound(nums:List[int],target:int) -> int:
        left = 0
        right = len(nums)
        #左闭右开区间
        while left < right:
            #因为right的指针是指在外面的。因此 停止条件是 left = right
            mid = left + (right - left) // 2
            if nums[mid] == target:
                #当mid 等于 target的时候。说明找到了target。但是我们是为了寻找左侧的边界
                # [--ttmtt--]
                # 现在我们想知道最左侧的 target的位置。 那么就应该舍弃右边的所有元素。
                # 也就是把right的指针位置更新到现在mid的位置
                # 但是我们已经知道 mid 等于 target了。那说明 right 右边的元素就不需要了 。 直接把 现在的窗口更新为 [left,mid)
                right = mid
            elif nums[mid] < target:
                #[----m-t--]
                #这时候 说明 左边的元素都是不需要的。因为 是左开右闭。那么 应该是 left_new = m +1  新区间是[mid+1, right)
                left = mid + 1
            elif nums[mid] > target:
                #[-t--m----]
                #这说明右边的元素都是不需要的。 因为是左开右闭。右边是开的 那么应该是 right = mid。 
                right = mid 
        return left 