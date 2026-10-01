class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        # Pair each height with its corresponding name
        paired = zip(heights, names)
        
        # Sort the pairs based on height in descending order (reverse=True)
        sorted_pairs = sorted(paired, reverse=True)
        
        # Extract and return just the names from the sorted pairs
        return [name for height, name in sorted_pairs]