class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        ma=0
        for i in range(len(nums)-1):
            if (nums[i+1]-nums[i])>ma:
                ma= (nums[i+1]-nums[i])
        return ma
        