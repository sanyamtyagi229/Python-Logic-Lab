class Solution:

  def countEven(self, num: int) -> int:
    count = 0
    for i in range(1, num + 1):
      current = i
      digit_sum = 0
      while current > 0:
        digit_sum += current % 10
        current //= 10

      if digit_sum % 2 == 0:
        count += 1
    return count