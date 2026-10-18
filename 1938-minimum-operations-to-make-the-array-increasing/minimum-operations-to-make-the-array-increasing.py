class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        
        # Iterate starting from the second element
        for i in range(1, len(nums)):
            # If the current element is not strictly greater than the previous one
            if nums[i] <= nums[i - 1]:
                # We need to increase nums[i] to be exactly nums[i-1] + 1
                increment = (nums[i - 1] + 1) - nums[i]
                operations += increment
                nums[i] = nums[i - 1] + 1
                
        return operations