class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        result = []
        s = "123456789"
        n = len(s)
        
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                num = int(s[i:i + length])
                if low <= num <= high:
                    result.append(num)
                elif num > high:
                    break  
        return result