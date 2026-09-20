class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, n = set([]), len(nums)
        for i in range(n-2):
            target = -nums[i]
            lhs, rhs = i+1, n-1
            while lhs < rhs:
                if nums[lhs] + nums[rhs] < target:
                    lhs += 1
                elif nums[lhs] + nums[rhs] > target:
                    rhs -= 1
                else:
                    ans.add((nums[i], nums[lhs], nums[rhs]))
                    rhs -= 1
        return [list(x) for x in ans]
