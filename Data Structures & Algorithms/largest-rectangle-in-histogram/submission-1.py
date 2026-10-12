class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stacks = []
        area = 0 
        for i , height in enumerate(heights):
            start = i 
            
            while stacks and stacks[-1][1] > height:
                index , height_stack = stacks.pop()
                area = max(area , (i - index) * height_stack)
                start = index 
            stacks.append((start, height))
        
        while stacks:
            index ,  height_stack = stacks.pop()
            area = max(area , (n - index) * height_stack)

        return area