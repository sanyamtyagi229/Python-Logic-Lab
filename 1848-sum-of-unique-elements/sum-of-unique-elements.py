class Solution(object):
    def sumOfUnique(self, nums: list[int]) -> int:
        counts = Counter(nums)
        return sum(num for num, freq in counts.items() if freq == 1)