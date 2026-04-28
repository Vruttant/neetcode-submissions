class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict() 

        for i in range(0, len(nums)):
            if hashmap.get(nums[i]) is not None: 
                return [hashmap.get(nums[i]), i]
            else:
                hashmap[target - nums[i]] = i 
        
        return []

        

