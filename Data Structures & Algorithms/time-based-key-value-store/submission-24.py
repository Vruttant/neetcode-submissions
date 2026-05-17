from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        sorted_list = self.cache[key]
        
        start, end = 0, len(sorted_list) - 1

        while start <= end:
            mid = (start + end) // 2

            if sorted_list[mid][0] == timestamp:
                return sorted_list[mid][1]
            elif sorted_list[mid][0] > timestamp: 
                end = mid - 1
            else:
                start = mid + 1 

        print(sorted_list)
        return sorted_list[end][1] if end >= 0 else ""

