class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        
        q = sum // 9
        r = sum % 9
        
        digits = ['9'] * q
        if r > 0:
            digits.append(str(r))
            
        digits.extend(['0'] * (num - len(digits)))
        
        return "".join(digits)