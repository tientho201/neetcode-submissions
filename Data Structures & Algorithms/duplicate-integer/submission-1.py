class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            temp = nums[i]
            if temp in hashMap:
                return True
            else:
                hashMap[nums[i]] = i   

        return False 