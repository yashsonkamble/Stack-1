"""
I implemented the solution using a monotonic decreasing stack and traversed the array twice to handle its circular nature. For each element, I check if it is the next greater element for the indices stored in the stack. If it is, I update the result with the current value. Indices are only pushed during the first pass to avoid duplicates.
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * len(nums)
        stack = []
        for i in range(2 * n):
            while stack and nums[i % n] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i % n]

            if i < n:
                stack.append(i)
        return result   