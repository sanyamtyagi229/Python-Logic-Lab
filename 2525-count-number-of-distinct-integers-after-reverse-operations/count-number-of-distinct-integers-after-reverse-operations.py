class Solution:

  def countDistinctIntegers(self, nums: list[int]) -> int:
    res = set(nums)
    for i in nums:
      rev = 0
      while i != 0:
        rev = rev * 10 + (i % 10)
        i //= 10
      res.add(rev)
    return len(res)