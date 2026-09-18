class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        c_positions = []
        for index in range(len(s)):
            if s[index] == c:
                c_positions.append(index)
        result = []
        for current_index in range(len(s)):

            shortest_distance = float('inf')
            for c_index in c_positions:
                current_distance = abs(current_index - c_index)
                if current_distance < shortest_distance:
                    shortest_distance = current_distance
            result.append(shortest_distance)
            
        return result