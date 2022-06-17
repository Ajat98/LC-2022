#https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
        
        #check array sizes, use hashmap for smaller array
        #Make num1 smaller array
        #make hashmap for n1
        #initialize insertion pointer k = 0
        #iterate along num2
        #if current num is in hash map and count is positive,copy number into num1[k] and increment k
        #decrement count in hash map
        #return first k elements of num1
        d = {}
        
        if len(nums1) > len(nums2):
            nums1, nums2, = nums2, nums1
        
        for i in nums1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        k = 0 #pointer for insertion
        
        for x in nums2:
            if x in d.keys() and d[x] > 0:
                nums1[k] = x  #insert copy at k
                k+= 1         #increment k by 1 to right
                d[x] -= 1     #decrement hashmap count
                
        return nums1[:k]       #return items up to k
