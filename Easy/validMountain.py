#https://leetcode.com/explore/featured/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)
        i = 0
        
        #left to right, check increasing
        while i+1 < n and arr[i] < arr[i+1]:
            i += 1
            
        #since peak cannot be on ends of array    
        if i == 0 or i == n-1:
            return False
        
        #decesnding from peak left to right
        while i+1 < n and arr[i] > arr[i+1]:
            i += 1
            
        if i == n-1: return True
            
        
        
