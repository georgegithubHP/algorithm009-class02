import heapq
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        class cmpObj:
            def __init__(self, priority, name):
                self.priority = priority
                self.name = name
            def __cmp__(self, other):
                if self.priority < other.priority:
                    return 1
                elif self.priority > other.priority:
                    return -1
                else:
                    return 0
        def zero():
            return 0
        hs, que, res  = defaultdict(zero), [], []
        for item in nums:
            hs[item] += 1
        for key, value in hs.items():
            heapq.heappush(que, cmpObj(value, key))
        while k > 0:
            item = heapq.heappop(que)
            res.append(item.name)
            k -= 1

        return res
