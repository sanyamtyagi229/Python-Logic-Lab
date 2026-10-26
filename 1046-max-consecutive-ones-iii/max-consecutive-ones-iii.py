class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=0
        maxl=0
        for r in range(len(nums)):
            if nums[r]==0:
                k=k-1
            if k<0:
                if nums[l]==0:
                    k=k+1
                l=l+1
            maxl=max(maxl,r-l+1)
        return maxl
            
        