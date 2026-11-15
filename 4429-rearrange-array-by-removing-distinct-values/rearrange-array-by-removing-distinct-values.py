class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        while nums:
            distinct_vals = sorted(list(set(nums)))
            for val in distinct_vals:
                ans.append(val)
                nums.remove(val)
                
        return ans