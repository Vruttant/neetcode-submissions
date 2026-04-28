class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0 
        end = len(heights) - 1
        max_water = 0 
        while start < end: 
            current_water = min(heights[start], heights[end]) * (end - start)
            max_water = max(current_water, max_water)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return max_water