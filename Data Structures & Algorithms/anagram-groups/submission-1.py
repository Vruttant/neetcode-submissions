class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = dict() 

        for string in strs:
            sorted_string = "".join(sorted(string))

            if cache.get(sorted_string):
                cache[sorted_string].append(string)
            else:
                cache[sorted_string] = [string]
            
        
        return list(cache.values())