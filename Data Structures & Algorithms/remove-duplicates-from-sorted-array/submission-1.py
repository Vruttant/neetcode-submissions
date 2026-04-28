class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tracker = sorted(list(set(nums)))
        print(tracker)

        for i in range(len(tracker)):
            nums[i] = tracker[i]
        
        return len(tracker)


