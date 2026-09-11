class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        valid_numbers = set()
        for i in range(n):
            if digits[i] == 0: 
                continue  
                
            for j in range(n):
                if i == j: 
                    continue  
                    
                for k in range(n):
                    if i == k or j == k: 
                        continue 
                        
                    if digits[k] % 2 == 0: 
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        valid_numbers.add(num)
                        
        return len(valid_numbers)