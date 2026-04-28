class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water= 0 
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                diff = j - i 
                border = min(heights[j], heights[i])
                trapped_water = diff * border 
                max_water = max(trapped_water, max_water)
        
        return max_water