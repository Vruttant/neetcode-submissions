class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""

        first_word = strs[0]
        for char_idx in range(len(first_word)):
            fw_slice = first_word[:char_idx + 1]
            print(fw_slice)

            for string in strs:
                if fw_slice not in string:
                    return longest_prefix
            
            longest_prefix = fw_slice
        
        return longest_prefix
        