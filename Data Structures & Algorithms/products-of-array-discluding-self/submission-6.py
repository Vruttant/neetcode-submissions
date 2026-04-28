class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # creating prefix_sum and suffix_sum
        prefix_sum = [0] * (len(nums) + 1)
        suffix_sum = [0] * (len(nums) + 1)
        prefix_sum[0] = suffix_sum[len(nums)] = 1
        # calculate prefix_sum

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] * nums[i - 1]
        
        for i in range(len(suffix_sum) - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] * nums[i]
        
        return [prefix_sum[i] * suffix_sum[i + 1] for i in range(len(nums))]

