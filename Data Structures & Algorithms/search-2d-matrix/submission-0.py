class Solution:
    def binarySearch(self, nums, target):
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True 
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = start + 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binarySearch(row, target):
                return True
        return False 