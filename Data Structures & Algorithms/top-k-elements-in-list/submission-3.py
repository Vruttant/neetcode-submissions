from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        res = []

        freq_map = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            res.append(freq_map[i][0])
        
        return res