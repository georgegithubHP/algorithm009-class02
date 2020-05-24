import collections
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length < 3: return 0
        res, idx = 0, 0
        stack = collections.deque()
        while idx < len(height):
            if len(stack) != 0 and height[idx] > height[stack[0]]:
                while len(stack) > 0 and height[stack[0]] <= height[idx]:
                    j = stack.popleft()
                    if len(stack) == 0:
                        break
                    plus = abs(min(height[stack[0]], height[idx]) - height[j]) * (idx - stack[0] - 1)
                    res += plus
            stack.appendleft(idx)
            idx += 1
        return res



