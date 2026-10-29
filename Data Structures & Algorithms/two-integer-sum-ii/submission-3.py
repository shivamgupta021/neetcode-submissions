class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        low = 0
        high = n - 1
        while low < high:
            ans = numbers[low] + numbers[high]
            if ans == target:
                return [low + 1, high + 1]
            if ans > target:
                high -= 1
            else:
                low += 1