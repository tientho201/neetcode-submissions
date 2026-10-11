class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for i in nums:
            groups[i] = groups.get(i, 0) + 1

        temp = sorted(groups, key=groups.get, reverse=True)

        return list(temp[:k])