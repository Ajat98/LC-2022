#https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #loop through arr and for each elem
        #search through hash table for current element, return true if found
        #put current element in hashtable
        #if size of hashtable larger than k, remove oldest item
        #return False
        
        d = {}
        
        for i in range(len(nums)):
            if nums[i] in d:
                return True #we have found duplicate
            else:
                d[nums[i]] = 1
            if len(d) > k: #must remove oldest item, or first item added
                d.pop(nums[i -k]) #this targets furthest item to the left when we hit the limit of k
                
        return False
            
        
