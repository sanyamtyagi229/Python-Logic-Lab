class Solution:

  def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
    ans = 0
    pens = 0
    while pens * cost1 <= total:
      rem = total - (pens * cost1)
      ans += (rem // cost2) + 1
      pens += 1
    return ans