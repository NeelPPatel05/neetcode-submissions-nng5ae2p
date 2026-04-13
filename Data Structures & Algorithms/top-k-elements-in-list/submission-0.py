class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        max = 0
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num]= counts[num] +1
        sorted_dict = dict(sorted(counts.items(), key=lambda x: x[1], reverse = True))
        return list(sorted_dict)[:k]


