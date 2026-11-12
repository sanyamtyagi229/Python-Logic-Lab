class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        c = []
        while i < j:
            a = nums[i]
            b = nums[j]
            avg = (a + b) / 2
            c.append(avg)
            i += 1
            j -= 1
        c.sort()
        
        k = 0
        for idx in range(1, len(c)):
            if c[idx - 1] != c[idx]:
                k += 1
        return k + 1 if len(c) > 0 else 0