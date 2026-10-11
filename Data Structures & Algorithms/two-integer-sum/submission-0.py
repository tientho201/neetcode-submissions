class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hashMap:
                return [hashMap[temp],i]
            else:
                hashMap[nums[i]] = i  