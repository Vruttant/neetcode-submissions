class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0 

        if len(s) <= 1: 
            return 1 

        i, j = 0, 0 
        max_len = 0
        while i <= len(s) - 1:
            visited = set([s[i]])
            j = i + 1
            while j <= len(s) - 1: 
                if s[j] in visited:
                    max_len = max(max_len, len(visited)) 
                    visited = set() 
                    break 
                else:
                    visited.add(s[j])
                    j += 1
            max_len = max(max_len, len(visited)) 
            i += 1
        return max_len




            
