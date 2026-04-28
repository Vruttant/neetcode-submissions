class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_sub_length = 0 
        for num in nums: 
            # check if the num has left neighbour 
            if (num - 1) not in nums:
                # means this is the starting of the sequence 
                sub_length = 1 
                while (num + 1) in nums:
                    sub_length += 1
                    num = num + 1

                longest_sub_length = max(longest_sub_length, sub_length)

        return longest_sub_length   
                
            
