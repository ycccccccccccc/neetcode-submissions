class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        note = collections.defaultdict(list)
        for i, char in enumerate(s):
            if len(note[char]) < 2:
                note[char].append(i)
            else:
                note[char][1] = i

        res = []
        currTail = -1
        for i, char in enumerate(s):
            if i > currTail:
                res.append(1)
                currTail = max(note[char])
            else:
                tail = max(note[char])
                currTail = max(tail, currTail)
                res[-1] += 1

        return res