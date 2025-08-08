#
# @lc app=leetcode.cn id=933 lang=python3
# @lcpr version=30202
#
# [933] 最近的请求次数
#

# @lc code=start
from queue import Queue 
class RecentCounter:
    def __init__(self):
        self.q = Queue()
    def ping(self, t: int) -> int:
        self.q.put(t)
        while self.q.queue[0] < t - 3000:
            self.q.get()
        
        return self.q.qsize()
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end



#
# @lcpr case=start
# ["RecentCounter", "ping", "ping", "ping", "ping"]\n[[], [1], [100], [3001], [3002]]\n
# @lcpr case=end

#

