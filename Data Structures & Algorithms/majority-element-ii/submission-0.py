from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cache = defaultdict(int)
        for elem in nums: 
            cache[elem] += 1
        
        ans = []
        threshold = len(nums) // 3
        for key, value in cache.items():
            if value > threshold:
                ans.append(key)
        
        return ans
