class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            picked, right = nums[mid], nums[-1]
            if picked == target:
                return mid
            elif target < picked <= right:
                r = mid - 1
            elif picked < target <= right:
                l = mid + 1
            elif right < target < picked:
                r = mid - 1
            elif right < picked < target:
                l = mid + 1
            elif target <= right < picked:
                l = mid + 1
            elif picked <= right < target:
                r = mid - 1
        return -1