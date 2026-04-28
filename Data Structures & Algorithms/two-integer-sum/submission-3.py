class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: target - nums[i]; value: i 
        cache = dict() 

        for i in range(len(nums)):
            if cache.get(nums[i]) is not None:
                return [cache.get(nums[i]), i]
            else:
                cache[target-nums[i]] = i
        
        return []