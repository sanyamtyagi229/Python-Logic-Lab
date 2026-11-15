class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=0
        while n>0:
            s=s+n%10
            n=n//10
        return s