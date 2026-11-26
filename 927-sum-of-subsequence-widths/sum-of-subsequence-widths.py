class Solution:

  def sumSubseqWidths(self, nums: list[int]) -> int:
    mod = 10**9 + 7
    n = len(nums)

    if n <= 1:
      return 0

    nums.sort()

    pw = [1] * n
    cur = 1
    for i in range(1, n):
      cur = (cur * 2) % mod
      pw[i] = cur

    ans = 0
    for i in range(n):
      left = pw[i]
      right = pw[n - 1 - i]
      diff = (left - right) % mod
      val = (nums[i] * diff) % mod
      ans = (ans + val) % mod

    return ans