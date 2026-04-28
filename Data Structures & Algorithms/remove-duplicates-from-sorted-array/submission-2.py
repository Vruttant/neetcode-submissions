class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  
        j = 1 

        while j <= len(nums) - 1:
            if nums[j - 1] == nums[j]:
                # duplicate, skip 
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1

        return i + 1


