class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count = {}
        for x in answers:
            if x not in count:
                count[x] = 0
            count[x] += 1
        total = 0

        for x in count:
            group_size = x + 1

            groups_needed = (
                count[x] + group_size - 1
            ) // group_size

            total += groups_needed * group_size

        return total