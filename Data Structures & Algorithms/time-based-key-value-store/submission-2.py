class TimeMap:

    def __init__(self):
        self.pairs = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pairs[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.pairs[key])-1
        if r == -1 or self.pairs[key][0][0] > timestamp: return ""
        if self.pairs[key][-1][0] < timestamp: return self.pairs[key][-1][1]

        while l <= r:
            m = (l+r)//2
            if self.pairs[key][m][0] > timestamp:
                r = m - 1
            elif self.pairs[key][m][0] == timestamp:
                return self.pairs[key][m][1]
            else:
                l = m + 1

        return self.pairs[key][l-1][1]
