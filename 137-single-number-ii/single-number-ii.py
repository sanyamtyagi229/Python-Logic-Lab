class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        for num, count in count_map.items():
            if count == 1:
                return num