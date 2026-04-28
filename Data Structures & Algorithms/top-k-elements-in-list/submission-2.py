class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums = [1,2,2,3,3,3] k = 2
        nums_cache = {1: 1, 2: 2, 3: 3}
        nums_cache_sorted = sorted(nums_cache, key=lambda item: item[1])
    

        """

        nums_cache = defaultdict(int) 
        for num in nums: 
            nums_cache[num] += 1 
        
        nums_cache_sorted = sorted(nums_cache, key=lambda item: nums_cache[item], reverse=True)
        return nums_cache_sorted[:k]