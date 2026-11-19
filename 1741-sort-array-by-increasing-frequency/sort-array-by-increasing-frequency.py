class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        sorted_items = sorted(freq.items(), key=lambda item: (item[1], -item[0]))

        result = []
        for x, c in sorted_items:
            result.extend([x] * c)

        return result