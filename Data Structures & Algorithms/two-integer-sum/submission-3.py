class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, num in enumerate(nums):
            delta = target - num
            if delta in mapping:
                return [mapping[delta], i]
            mapping[num] = i
        