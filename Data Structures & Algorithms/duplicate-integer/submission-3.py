class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()

        for num in nums:
            if hashmap.get(num) is not None:
                return True
            hashmap[num] = 1
        
        return False
