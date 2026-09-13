class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            if num in dic:
                return [dic[num], idx]
            dic[target - num] = idx
        