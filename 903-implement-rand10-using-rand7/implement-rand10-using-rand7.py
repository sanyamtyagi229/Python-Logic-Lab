# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            
            # Generates a uniform distribution from 1 to 49
            idx = col + (row - 1) * 7 
            
            # Reject numbers from 41 to 49 to maintain a uniform distribution for 1-10
            if idx <= 40:
                return 1 + (idx - 1) % 10