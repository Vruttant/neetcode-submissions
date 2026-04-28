from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = set()
        length = len(nums)
        for num in nums:
            if num in counts:
                continue 
        
            if nums.count(num) > length // 3: 
                counts.add(num)
        return list(counts)

