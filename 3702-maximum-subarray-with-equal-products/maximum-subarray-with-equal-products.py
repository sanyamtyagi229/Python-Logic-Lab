class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        k=0
        for i in range(n):
            gc=0
            lc=1
            p=1
            for j in range(i,n):
                x=nums[j]
                p*=x
                gc=x if j==i else math.gcd(gc,x)
                lc=math.lcm(lc,x)
                if p==lc*gc:
                    l=j-i+1
                    k=max(l,k)
        return k
            
        