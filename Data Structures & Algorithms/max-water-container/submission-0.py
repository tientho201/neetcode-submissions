class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n , m = 0 , len(heights) - 1 
        result = 0 
        while n < m:
            if heights[n] < heights[m]:
                result = max(result , (m - n)*  heights[n])
                n += 1 
            else:
                result = max(result , (m - n) *  heights[m])
                m -= 1 
        return result