import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for item in strs:
            res[tuple(sorted(item))].append(item)
        return res.values()
