class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        es=0
        os=0
        for i in range(len(nums)):
            if i%2==0:
                es+=nums[i]
            else:
                os+=nums[i]
        return es-os
        