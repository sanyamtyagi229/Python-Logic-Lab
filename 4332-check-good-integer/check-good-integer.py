class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        ds=0
        ss=0
        while n!=0:
            d=n%10
            ds+=d
            ss+=d**2
            n=n//10
        if ss-ds>=50:
            return True
        else:
            return False
        