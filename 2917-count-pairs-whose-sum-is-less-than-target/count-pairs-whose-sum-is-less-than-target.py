class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i<j and nums[i]+nums[j]<target:
                    c=c+1
        return c      