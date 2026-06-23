class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        note = collections.defaultdict(int)
        for i, char in enumerate(s):
            note[char] = i

        res = []
        currTail = -1
        for i, char in enumerate(s):
            if i > currTail:
                res.append(1)
            else:
                res[-1] += 1
            currTail = max(note[char], currTail)

        return res