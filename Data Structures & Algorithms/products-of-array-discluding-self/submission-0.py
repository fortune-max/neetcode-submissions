class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prfx_arr, sfx_arr = [0] * len(nums), [0] * len(nums)
        prfx_arr[0], sfx_arr[-1] = nums[0], nums[-1]
        num_ct = len(nums)
        for i in range(1, num_ct):
            prfx_arr[i] = prfx_arr[i-1] * nums[i]
            sfx_arr[-i-1] = sfx_arr[-i] * nums[-i-1]
        ans = [0] * num_ct
        for i in range(num_ct):
            lhs = 1 if i == 0 else prfx_arr[i-1]
            rhs = 1 if i == num_ct-1 else sfx_arr[i+1]
            ans[i] = lhs * rhs
        return ans
