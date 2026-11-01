class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()  # Step 1: Sort the array
        count = 0
        i = 0
        n = len(nums)
        while i < n:   
            count += 1 
            min_val = nums[i]
            j = i
            while j < n and nums[j] - min_val <= k:
                j += 1
            i = j
            
        return count