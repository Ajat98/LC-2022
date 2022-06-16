#https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        
        #pop off digits 1 by 1 and square them adding to total sum
        def getNext(n):
            total = 0
            while n > 0: #must be above 0 or else loops infinitely if equal to 0
                n, d = divmod(n, 10) #output is quotient, and remainder. Divide by 10 to get new n, the remainder is our digit popped off
                total += d ** 2
            return total
        
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = getNext(n)
            
            
        return n == 1
        
        
