
class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        maximum = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count = count + 1
            else:
                count = 1

            if count > maximum:
                maximum = count

        return maximum
