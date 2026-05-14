class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        last_valid_k = max(piles)

        start = 1 
        end = last_valid_k

        while start <= end: 
            mid = (start + end) // 2

            hours = 0
            
            for pile in piles:
                hours += math.ceil(float(pile)/mid)

            if hours <= h:
                last_valid_k = mid 
                end =  mid - 1
            else:
                start = mid + 1
        
        return last_valid_k
            



