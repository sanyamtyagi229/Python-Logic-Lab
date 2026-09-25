class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(n):
            arr.append(nums[i])      # Append the x element from the first half
            arr.append(nums[i + n])  # Append the y element from the second half
        return arr