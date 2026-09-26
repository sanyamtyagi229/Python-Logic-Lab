class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        dictionary = {}

        for pair in knowledge:
            dictionary[pair[0]] = pair[1]

        answer = ""
        i = 0

        while i < len(s):

            if s[i] != '(':
                answer += s[i]
                i += 1

            else:
                i += 1
                key = ""

                while s[i] != ')':
                    key += s[i]
                    i += 1

                if key in dictionary:
                    answer += dictionary[key]
                else:
                    answer += "?"

                i += 1

        return answer