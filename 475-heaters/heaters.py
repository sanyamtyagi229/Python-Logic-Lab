from bisect import bisect_left


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()
        ans = 0

        for house in houses:
            idx = bisect_left(heaters, house)
            if idx < len(heaters):
                rd = heaters[idx] - house
            else:
                rd = float("inf")
            if idx > 0:
                ld = house - heaters[idx - 1]
            else:
                ld = float("inf")
            closest = min(ld, rd)
            ans = max(ans, closest)

        return ans