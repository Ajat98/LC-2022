#https://leetcode.com/explore/featured/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        d = {}
        
        for i in range(len(arr)):
                
            if arr[i] * 2 in d.values():
                return True
            
            elif arr[i] % 2 == 0 and arr[i] / 2 in d.values():
                return True
            
            d[i] = arr[i]
            print(d)
            
        return False
        
                
    
        
