class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) / 2
            if nums[mid-1] > nums[mid]: return nums[mid]
            if mid+1 == len(nums) : return nums[0]
            if nums[mid] > nums[mid+1]: return nums[mid+1]
            if nums[0] < nums[mid]: l = mid + 1
            else: r = mid - 1