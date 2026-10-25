class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        sorted_nums = sorted(
            freq,
            key=freq.__getitem__,
            reverse=True
        )

        return sorted_nums[:k]