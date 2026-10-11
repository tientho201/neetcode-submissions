class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n 
        subfix = [1] * n 
        i = 1
        while i < n :
            prefix[i] = prefix[i - 1] * nums[i - 1]
            i += 1
        for j in range(n - 2 , -1 , -1):
            subfix[j] = nums[j + 1 ] * subfix[j + 1 ]
        result = []
        for x in range( 0 , n ):
            result.append(prefix[x] * subfix[x])
        return result