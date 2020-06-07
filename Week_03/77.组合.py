class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def recurse(n, k, m):
            if k == 0:
                res.append(m)
                return
            for i in range(1, n+1):
                if k - 1 == i or i in m: continue
                recurse(i, k-1, m+[i])
        recurse(n, k, [])
        return recurse
