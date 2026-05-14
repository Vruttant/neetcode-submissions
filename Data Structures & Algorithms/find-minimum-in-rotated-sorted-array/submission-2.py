class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        smallest = float('inf')
        while start <= end: 
            mid = (start + end) // 2

            if nums[start] <= nums[mid]:
                smallest = min(nums[start], smallest)
                start = mid + 1
            else:
                smallest = min(nums[mid], smallest)
                end = mid - 1
        
        return smallest