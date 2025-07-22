"""
I used a decreasing monotonic stack to track indices of unresolved temperatures. For each temperature, I compare it with the top of the stack. If the current temperature is higher, I pop from the stack and compute the difference in indices to find the wait time. This ensures each temperature is processed only once.
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                index, _ = stack.pop()
                result[index] = i - index
            stack.append((i, temp))
        return result