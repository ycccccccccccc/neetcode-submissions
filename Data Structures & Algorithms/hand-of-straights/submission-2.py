class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1: return True
        hand.sort()
        note = collections.defaultdict(list)
        currNum = hand[0]
        for num in hand:
            print(note)
            if currNum != num and note[num-2]:
                return False
            if note[num-1]:
                p = note[num-1].pop()
                if p < groupSize - 1:
                    note[num].append(p+1)
            else:
                note[num].append(1)
            currNum = num
        if note[hand[-1]]:
            return False
        return True