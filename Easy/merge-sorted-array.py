class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy = nums1[:m] #end at first m values
        
        #two reading pointer and one write
        p1 = 0
        p2 = 0
        
        #compare elems from num1copy to num2, write smallest to nums1
        for x in range(n+m):
            #first check pointers are within boundaries of arrays
            #if p2 is out of bounds of nums2, OR if p1 still within bounds, and element is smaller than pointer in nums2s --> copy from nums1 copy
            if p2 >=n or (p1 < m and copy[p1] <= nums2[p2]):  
                
                nums1[x] = copy[p1]
                p1 += 1 #increment after a value is copied
            else:
                nums1[x] = nums2[p2]
                p2 += 1
            
        
            
