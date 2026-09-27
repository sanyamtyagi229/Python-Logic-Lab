class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        for c in operations:
            if c.lstrip('-').isdigit():
                record.append(int(c))
            elif c == '+':
                k = record[-1] + record[-2]
                record.append(k)
            elif c == 'C':
                record.pop()
            elif c == 'D':
                x = 2 * record[-1]
                record.append(x)
        return sum(record)