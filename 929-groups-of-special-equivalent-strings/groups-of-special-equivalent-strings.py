class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        seen = set()

        for word in words:
            even = []
            odd = []

            for idx in range(len(word)):
                if idx % 2 == 0:
                    even.append(word[idx])
                else:
                    odd.append(word[idx])

            even.sort()
            odd.sort()

            key = ("".join(even), "".join(odd))
            seen.add(key)

        return len(seen)