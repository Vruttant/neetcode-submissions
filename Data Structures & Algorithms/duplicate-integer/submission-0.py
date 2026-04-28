class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict() 
        for digit in nums:
            if hashmap.get(digit):
                return True
            else:
                hashmap[digit] = 1 
        
        return False 