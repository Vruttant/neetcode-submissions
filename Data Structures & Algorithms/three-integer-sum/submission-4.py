class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and s_nums[i] == s_nums[i - 1]:
                continue

            start = i + 1
            end = len(nums) - 1



            while start < end: 
                summation = s_nums[i] + s_nums[start] + s_nums[end]

                if summation == 0:
                    res.append([s_nums[i], s_nums[start], s_nums[end]])
                    start += 1
                    end -= 1
                    
                    while start < end and s_nums[start] == s_nums[start - 1]:
                        start += 1

                    # skip duplicate end
                    while start < end and s_nums[end] == s_nums[end + 1]:
                        end -= 1


                elif summation > 0:
                    end -= 1
                else:
                    start += 1
        
        return res 