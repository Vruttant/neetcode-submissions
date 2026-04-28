class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l_seq_len = 0 

        s_nums = set(nums)
        
 
        for num in nums:
            if num - 1 in s_nums: 
                continue 
            else:
                # this means this is a start of sequence
                l_seq = 1
                integer = num + 1
                while integer in s_nums:
                    l_seq += 1
                    integer += 1
                
                l_seq_len = max(l_seq, l_seq_len)
        
        return l_seq_len

            

