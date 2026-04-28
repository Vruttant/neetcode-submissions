class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_with_zero =  1
        product_without_zero = 1 
        zero_count = 0 
        for num in nums:
            product_with_zero *= num 
            if num == 0:
                zero_count += 1
                continue
            else:
                product_without_zero *= num

            
        
        if zero_count > 1:
            return [0] * len(nums)

        nums_copy = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] != 0:
                nums_copy[i] = product_with_zero//nums[i]
            else:
                nums_copy[i] = product_without_zero

        return nums_copy