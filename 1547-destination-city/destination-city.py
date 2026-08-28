class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen=set()
        for s,e in paths:
            seen.add(s)
        for s,e in paths:
            if not e in seen:
                return e
