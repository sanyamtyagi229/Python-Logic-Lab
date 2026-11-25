class Solution:

  def longestNiceSubstring(self, s: str) -> str:
    best = ""
    n = len(s)

    for i in range(n):
      for j in range(i, n):
        sub = s[i : j + 1]
        if self.is_nice(sub) and len(sub) > len(best):
          best = sub

    return best

  def is_nice(self, sub: str) -> bool:
    seen = set()

    for ch in sub:
      seen.add(ch)

    for ch in seen:
      if ch.swapcase() not in seen:
        return False

    return True