class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for i in nums:
            if i in groups:
                groups[i] += 1 
            else:
                groups[i] = 1
        result = []
        for x in groups.keys():
            if groups[x] >= k:
                result.append(x)
        return result