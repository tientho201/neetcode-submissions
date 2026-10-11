class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        result = 0 
        for x in set_nums:
            if x - 1 not in set_nums:
                current = x 
                length = 1 

                while current +1 in set_nums:
                    current += 1
                    length += 1 
                result = max(result,length) 
        return result