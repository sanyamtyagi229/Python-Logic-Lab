class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 0
        j = len(nums) - 1
        p = 0
        q = 0
        while (i + 1) < len(nums) and nums[i] < nums[i+1]:
            p = i + 1
            i = i + 1
        while (j - 1) >= 0 and nums[j] > nums[j-1]:
            q = j - 1
            j = j - 1
        if p == 0 or q == len(nums) - 1 or p >= q:
            return False
        for k in range(p, q):
            if nums[k] <= nums[k+1]:
                return False
                
        return True