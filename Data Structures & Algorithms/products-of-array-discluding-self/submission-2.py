class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_product = 1
        nums_product_without_zeros = 1  
        zero_count = 0 
        for num in nums:
            nums_product *= num

            if num != 0:
                nums_product_without_zeros *= num 
            elif num == 0: 
                zero_count += 1 

        if zero_count > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            ith_num = nums[i]
            if not ith_num: 
                nums[i] = nums_product_without_zeros
                continue
            nums[i] = nums_product // ith_num

        return nums