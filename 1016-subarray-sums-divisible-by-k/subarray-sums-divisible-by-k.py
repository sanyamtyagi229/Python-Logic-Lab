class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_count = {0: 1}

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in remainder_count:
                count += remainder_count[remainder]
            else:
                remainder_count[remainder] = 0

            remainder_count[remainder] += 1

        return count