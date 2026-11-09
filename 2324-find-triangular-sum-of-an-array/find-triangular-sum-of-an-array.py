class Solution(object):
    def triangularSum(self, nums):
        n=len(nums)
        for i in range(n-1):
            level=[]
            for i in range(len(nums)-1):
                level.append((nums[i]+nums[i+1])%10)
            nums=level
        return nums[0]

        