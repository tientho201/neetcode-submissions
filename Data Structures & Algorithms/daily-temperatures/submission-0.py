class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n 
        stacks = []
        for i in range(n):
            while stacks and temperatures[i] > temperatures[stacks[-1]]:
                prev = stacks.pop()
                result[prev] = i - prev 
            stacks.append(i)
        return result