
class Solution:
    def maxCount(self, banned, n, maxSum):

        banned_set = set(banned)

        count = 0
        total = 0

        for i in range(1, n + 1):

            if i in banned_set:
                continue

            if total + i > maxSum:
                break

            total += i
            count += 1

        return count
