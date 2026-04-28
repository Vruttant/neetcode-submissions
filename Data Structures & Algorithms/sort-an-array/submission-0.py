

class Solution:
    def merge(self, array, low, mid, high):
        temp = []

        start = low 
        end = mid + 1

        while (start <= mid and end <= high):
            if array[start] <= array[end]:
                temp.append(array[start])
                start += 1
            else:
                temp.append(array[end])
                end += 1

        while start <= mid:
            temp.append(array[start])
            start += 1
        
        while end <= high:
            temp.append(array[end])
            end += 1
        
        for i in range(low, high + 1):
            array[i] = temp[i - low]
        


    def mergeSortHelper(self, array, low, high):
        if low >= high:
            return 
        mid = (low + high) // 2

        self.mergeSortHelper(array, low, mid)
        self.mergeSortHelper(array, mid + 1, high)
        self.merge(array, low, mid, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSortHelper(nums, 0, len(nums) - 1)
        return nums
        