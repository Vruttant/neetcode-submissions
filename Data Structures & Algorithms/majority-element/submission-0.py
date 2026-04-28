from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if count[num] > threshold:
                return num 
        
        return 0 
        
                    