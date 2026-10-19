class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        a=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                a.append(i)
        return a
        