class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # Convert to strings and pad with leading zeros until length is 4
        s1 = str(num1).zfill(4)
        s2 = str(num2).zfill(4)
        s3 = str(num3).zfill(4)
        
        key_str = ""
        
        # Iterate through the 4 characters from left to right
        for i in range(4):
            # Find the minimum character at the current index and append it
            key_str += min(s1[i], s2[i], s3[i])
            
        # Convert back to an integer to naturally drop any leading zeros
        return int(key_str)