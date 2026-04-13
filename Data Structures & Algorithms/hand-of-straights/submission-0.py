class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        sorted_hand = sorted(hand)
        count = {}
        for num in sorted_hand:
            count[num] = count.get(num, 0) + 1
        for num in sorted_hand:
            if count[num] > 0:
                for j in range(groupSize):
                    if count.get(num + j, 0) > 0:
                        count[num + j] -= 1
                    else:
                        return False
        return True
