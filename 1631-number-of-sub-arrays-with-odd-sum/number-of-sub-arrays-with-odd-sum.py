class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        total = 0
        even= 0
        odd = 0
        
        for num in arr:
            if num % 2 == 1:
                even,odd=odd,even
                odd += 1
            else:
                even += 1
                
            total =  (total+ odd) % MOD
            
        return total