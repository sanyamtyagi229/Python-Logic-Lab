class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        maxs=0
    
        while(i<j):
            s=nums[i]+nums[j]
            maxs=max(maxs,s)
            i=i+1
            j=j-1
        return maxs

        