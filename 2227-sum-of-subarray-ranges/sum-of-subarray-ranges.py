class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        s=0
        n=len(nums)
        for i in range(n):
            large=nums[i]
            small=nums[i]
            for j in range(i+1,n):
                large=max(large,nums[j])
                small=min(small,nums[j])
                s+=large-small
        return s
        