class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        # Map the ruleKey to the corresponding index
        key_map = {"type": 0, "color": 1, "name": 2}
        idx = key_map[ruleKey]
        
        # Count how many items match the ruleValue at the given index
        return sum(1 for item in items if item[idx] == ruleValue)