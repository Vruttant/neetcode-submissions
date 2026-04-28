class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1.copy() 
        ptr1 = 0
        ptr2 = 0 
        ptr3 = 0 


        while ptr1 < m and ptr2 < n:
            if nums1_copy[ptr1] < nums2[ptr2]:
                nums1[ptr3] = nums1_copy[ptr1]
                ptr1 += 1
                ptr3 += 1 
            elif nums1_copy[ptr1] > nums2[ptr2]:
                nums1[ptr3] = nums2[ptr2]
                ptr2 += 1
                ptr3 += 1
            else:
                nums1[ptr3] = nums1[ptr1]
                ptr3 += 1
                nums1[ptr3] = nums2[ptr2]
                ptr3 += 1
                ptr2 += 1
                ptr1 += 1
        
        while ptr1 < m:
            nums1[ptr3] = nums1_copy[ptr1]
            ptr3 += 1
            ptr1 += 1
        
        while ptr2 < n: 
            nums1[ptr3] = nums2[ptr2]
            ptr3 += 1
            ptr2 += 1
        
        
