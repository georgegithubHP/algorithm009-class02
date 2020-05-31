from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(nums)
        if size == 0:
            return []
        res = []
        window = deque()
        for i in range(size):
            if i >= k and i - k == window[0]:
                window.popleft()
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)
            if i >= k-1:
                res.append(nums[window[0]])
        return res
