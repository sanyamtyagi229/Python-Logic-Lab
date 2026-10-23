
class Solution:
    def candy(self, ratings):
        n = len(ratings)

        total = 1
        up = 0
        down = 0
        peak = 0

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                down = 0
                total += 1 + up

            elif ratings[i] == ratings[i - 1]:
                up = 0
                down = 0
                peak = 0
                total += 1

            else:
                up = 0
                down += 1
                total += 1 + down

                if peak >= down:
                    total -= 1

        return total
