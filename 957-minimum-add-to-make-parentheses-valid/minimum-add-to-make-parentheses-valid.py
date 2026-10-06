class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        oc = 0
        ans = 0
        for char in s:
            if char == '(':
                oc += 1
            elif char == ')':
                if oc > 0:
                    oc -= 1
                else:
                    ans += 1
        return ans + oc