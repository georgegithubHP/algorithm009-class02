class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        for index, i in enumerate(nums):
            if i == 0 and nums[anchor] != 0:
                anchor = index
            else:
                nums[index] , nums[anchor] = nums[anchor], nums[index]
                
            if nums[anchor] != 0:
                anchor += 1
            
        return nums