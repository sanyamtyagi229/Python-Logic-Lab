class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            s = cnt = 0
            if i > 0:
                s += nums[i - 1]
                cnt += 1
            if i + 1 < n:
                s += nums[i + 1]
                cnt += 1
            if cnt == 0 or nums[i] * cnt >= s:
                ans += 1
        return ans