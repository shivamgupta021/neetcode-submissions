class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = deque()
        stack.append([temperatures[0], 0])
        result = [0] * n

        for i in range(n):
            top = stack[-1]
            temp, idx = top[0], top[1]

            while temperatures[i] > temp and stack:
                result[idx] = i - idx
                stack.pop()

                if stack:
                    top = stack[-1]
                    temp, idx = top[0], top[1]
            
            stack.append([temperatures[i], i])
        
        return result

