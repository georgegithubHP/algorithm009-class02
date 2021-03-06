class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) / 2
            elem = matrix[mid/n][mid%n]
            if elem == target:
                return True
            if elem < target:
                l = mid + 1
            else:
                r = mid - 1
        return False