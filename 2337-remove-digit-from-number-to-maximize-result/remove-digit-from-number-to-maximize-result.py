class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_result = ""
        for i in range(len(number)):
            # When we find the target digit...
            if number[i] == digit:
                candidate = number[:i] + number[i+1:]
                if candidate > max_result:
                    max_result = candidate
        return max_result