class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_count = {0: 1}

        for num in nums:
            prefix_sum += num
            needed = prefix_sum - k

            if needed in prefix_count:
                count += prefix_count[needed]

            if prefix_sum not in prefix_count:
                prefix_count[prefix_sum] = 0

            prefix_count[prefix_sum] += 1

        return count