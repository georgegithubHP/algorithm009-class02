class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        """
        dp[i][j]:M[i][j] = 0: max(d[i-1][j], d[i][j-1])
                 M[i][j] = 1: max(d[i-1][j], d[i][j-1]) + 1(if M[i-1][j] == 0 and M[i][j-1] ==0 )
        """
        n = len(M)
        dp = [[1 for _ in range(n)] for _ in range(n) ]
        for i in range(1, n):
            for j in range(1, n):
                if M[i][j] == 1 and M[i-1][j] == 0 and M[i][j-1] == 0:
                    step = 1
                else:
                    step = 0
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + step

        return dp[n-1][n-1]
