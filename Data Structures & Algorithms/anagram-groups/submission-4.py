from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            list_s = list(s)
            list_s.sort()

            res[tuple(list_s)].append(s)
        
        return list(res.values())