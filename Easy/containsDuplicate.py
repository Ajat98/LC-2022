#https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        d = {}
        
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 1
        return False
        
