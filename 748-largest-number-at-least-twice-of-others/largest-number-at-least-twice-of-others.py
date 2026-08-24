class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        mi=nums.index(m)
        nums.sort()
        if (nums[-2]*2)<=m:
            return mi
        else:
            return -1

        
        