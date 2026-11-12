class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        distinct_avgs = set()
        
        while i < j:
            avg = (nums[i] + nums[j]) / 2.0
            distinct_avgs.add(avg)
            i += 1
            j -= 1
            
        return len(distinct_avgs)