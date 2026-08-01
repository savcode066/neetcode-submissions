class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                stackInd, stackTemp = stack.pop()
                result[stackInd] = i - stackInd

            stack.append([i, temperatures[i]])
        return result