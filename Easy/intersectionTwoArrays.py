#https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        
        c = a.intersection(b)
        
        return c
