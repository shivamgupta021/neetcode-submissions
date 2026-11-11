class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                result[stack[-1][1]] = idx - stack[-1][1]
                stack.pop()
            
            stack.append([temp, idx])
        
        return result

