class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        start = 1
        end = k
        if k < 0:
            start = n + k
            end = n - 1
        current_sum = 0
        for i in range(start, end + 1):
            current_sum += code[i % n]
        for i in range(n):
            res[i] = current_sum
            current_sum -= code[start % n]
            start += 1
            end += 1
            current_sum += code[end % n]
            
        return res