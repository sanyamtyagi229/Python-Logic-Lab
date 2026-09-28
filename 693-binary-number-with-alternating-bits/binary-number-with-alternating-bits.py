class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x=n&1
        n=n>>1
        while n>0:
            bit=n&1
            if bit==x:
                return False
            else:
                x=bit
            n=n>>1
        return True
            

        