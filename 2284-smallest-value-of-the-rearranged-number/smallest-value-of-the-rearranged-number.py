class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        if num > 0:
            # Sort digits in ascending order
            digits = sorted(str(num))
            
            # Find the first non-zero digit to avoid leading zeros
            for i in range(len(digits)):
                if digits[i] != '0':
                    # Swap the first non-zero digit with the leading zero
                    digits[0], digits[i] = digits[i], digits[0]
                    break
                    
            return int(''.join(digits))
        else:
            # For negative numbers, sort in descending order to minimize the value
            digits = sorted(str(abs(num)), reverse=True)
            return -int(''.join(digits))