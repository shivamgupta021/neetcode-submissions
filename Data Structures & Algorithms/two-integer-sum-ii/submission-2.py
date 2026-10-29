class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i, num in enumerate(numbers):
            fixture = target - num
            low = i + 1
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == fixture:
                    return [i + 1, mid + 1]
                if numbers[mid] < fixture:
                    low = mid + 1
                else:
                    high = mid - 1