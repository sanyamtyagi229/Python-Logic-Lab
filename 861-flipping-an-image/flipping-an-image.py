class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        # Create a new list to store our resulting matrix
        result = []
        for row in image:
            reversed_row = row[::-1]
            inverted_row = []
            for val in reversed_row:
                if val == 0:
                    inverted_row.append(1)
                else:
                    inverted_row.append(0)
            result.append(inverted_row)
            
        return result