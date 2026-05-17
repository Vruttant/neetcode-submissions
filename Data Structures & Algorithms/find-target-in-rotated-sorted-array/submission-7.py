class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 2:
            try:
                idx = nums.index(target)
            except ValueError:
                idx = -1 
            return idx 

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target: 
                return mid 
            elif nums[start] <= nums[mid]:
                # is the target in the sorted half? 
                if nums[start] <= target < nums[mid]: 
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # is the target in the right sorted half? 
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            

        return -1 
