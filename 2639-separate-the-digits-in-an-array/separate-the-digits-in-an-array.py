class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        a = []
        for num in nums:
            for digit in str(num):
                a.append(int(digit))
        return a
        