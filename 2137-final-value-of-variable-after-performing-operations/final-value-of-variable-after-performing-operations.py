class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for a in operations:
            if "--" in a:
                x -= 1
            else:
                x += 1
        return x