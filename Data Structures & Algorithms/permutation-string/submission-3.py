from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        og_cache = defaultdict(int)
        for ch in s1:
            og_cache[ch] += 1



        window_size = len(s1)

        l = 0 
        r = l + window_size # 2 in 1st tc


        while r <= len(s2): 
            cache = defaultdict(int)
            for i in range(l, r):
               cache[s2[i]] += 1

            if cache == og_cache:
                return True 

            l += 1
            r = l + window_size 

            print(cache)
        return False