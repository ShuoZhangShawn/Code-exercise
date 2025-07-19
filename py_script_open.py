
from typing import List
class Solution:
	def search(self,nums:List[int],target:int) -> int:
		left = 0
		right = len(nums)
		# right 的指针指向索引外。所以是左开右闭区间。 终止条件为 left = right:
		
		while left < right:
			mid = left + (right - left) //2
			if nums[mid] == target:
				return mid 
			elif nums[mid] > target:
			 #数组中间大于 target。 说明数组mid的右边完全没有 target。更新右端点
			 #[----t--m-----]
			 # right = mid - 1
			 	right = mid 
			 # 已经知道 mid 大于target了。因此 mid 不会在更新后的搜索范围内
			elif nums[mid] < target:
			 #数组中间小于 target。 说明数组mid的 左边会完全没有 target。这样就更新左端点
			 # [------m--t---]
				left = mid + 1
		return -1
				
				
