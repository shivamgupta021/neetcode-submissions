class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            required =  target - num
            if required in lookup:
                return [lookup[required] , i]
            lookup[num] = i