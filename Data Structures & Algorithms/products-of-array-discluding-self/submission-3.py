class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # need to solve this in O(n) space time  complexity 
        # first we need to create a prefix array such that each entry will have multiplaction of entries before ith index 
        # secon we need to create a postfix array such that each entry before will have the multiplication of entries before that 
        

        prefix_array = [1] * len(nums) 
        for i in range(1,len(nums)):
            prefix_array[i] = prefix_array[i - 1] * nums[i - 1]
        
        print(prefix_array)

        postfix_array = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            postfix_array[i] = postfix_array[i + 1] * nums[i + 1]
        
        result = [1] * len(nums) 
        for i in range(len(result)):
            result[i] = prefix_array[i] * postfix_array[i]
        
        return result