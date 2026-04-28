class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0 
        end = len(numbers) - 1

        while start < end: 
            computation = (numbers[start] + numbers[end])
            if computation == target:
                return [start + 1, end + 1] 
            
            elif computation < target: 
                start += 1
            
            else:
                end -= 1 
        
