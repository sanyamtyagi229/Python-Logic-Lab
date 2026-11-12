import random

class Solution:

    def __init__(self, nums: list[int]):
        self.original = list(nums)
        self.array = list(nums)

    def reset(self) -> list[int]:
        self.array = list(self.original)
        return self.array

    def shuffle(self) -> list[int]:
        aux = list(self.array)
        n = len(aux)
        for i in range(n - 1, 0, -1):
            j = random.randrange(0, i + 1)
            aux[i], aux[j] = aux[j], aux[i]
        return aux