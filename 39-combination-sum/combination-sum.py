class Solution:

  def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
    ans = []
    path = []

    def backtrack(start, remaining):
      if remaining == 0:
        ans.append(path.copy())
        return
      if remaining < 0:
        return

      for i in range(start, len(candidates)):
        path.append(candidates[i])
        backtrack(i, remaining - candidates[i])
        path.pop()

    backtrack(0, target)
    return ans