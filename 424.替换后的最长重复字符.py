#
# @lc app=leetcode.cn id=424 lang=python3
# @lcpr version=30201
#
# [424] 替换后的最长重复字符
#

# @lc code=start
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right = 0
        left = 0
        n = len(s)
        window = defaultdict(int)
        maxCount = 0
        res = 0 

        while right < n:
            window[s[right]] += 1
            maxCount = max(maxCount, window[s[right]])
            #贪心算法 每次窗口扩大时，我们只看当前加入的字符 c，看看它是不是当前最多的。
            #如果它更“多”，就更新 maxCount。
            right += 1

            while right - left - maxCount > k:
                window[s[left]] -= 1
                left += 1
            res = max(res, right - left)
        return res
        
# @lc code=end



#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

# @lcpr case=start
# "AABABBA"\n1\n
# @lcpr case=end

#

