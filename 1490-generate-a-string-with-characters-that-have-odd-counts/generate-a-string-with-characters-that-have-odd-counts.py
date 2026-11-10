class Solution:
    def generateTheString(self, n: int) -> str:
        a=""
        if n%2==1:
            while n!=0:
                a+="a"
                n-=1
        else:
            while n!=1:
                a+="a"
                n=n-1
            a+="b"
        return a
        