class Solution:

  def maxSum(self, nums: List[int]) -> int:
    groups = {}
    for num in nums:
      max_d = max(str(num))
      if max_d not in groups:
        groups[max_d] = []
      groups[max_d].append(num)

    max_total_sum = -1
    for max_d, numbers in groups.items():
      if len(numbers) >= 2:
        numbers.sort(reverse=True)
        current_sum = numbers[0] + numbers[1]
        max_total_sum = max(max_total_sum, current_sum)

    return max_total_sum