class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n , m = 0 , len(nums) - 1 
        while n <= m:
            mid = n + (m - n ) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                m = mid - 1 
            else:
                n = mid + 1 
        return  -1