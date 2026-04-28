class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_of_nums = len(nums)
        for i in range(0, len_of_nums - 1):
            for j in range(i + 1, len_of_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []
