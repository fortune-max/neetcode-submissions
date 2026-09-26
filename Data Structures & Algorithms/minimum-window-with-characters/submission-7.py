class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c_to_idx = lambda c: (o := ord(c)) - (71 if o > 96 else 65)
        chk = lambda: all((s_freq >= t_freq for t_freq, s_freq in zip(t_arr, s_arr)))

        s_arr, t_arr, s_ct, t_ct = [0] * 52, [0] * 52, len(s), len(t)
        l, r, ans, ans_str = 0, t_ct - 1, float("inf"), (0, 0)

        if t_ct > s_ct:
            return ""

        for idx in range(t_ct):
            t_arr[c_to_idx(t[idx])] += 1
            s_arr[c_to_idx(s[idx])] += 1
        satisfied = chk()

        while l <= r:
            while satisfied:
                if r-l+1 < ans:
                    ans, ans_str = r-l+1, (l, r+1)
                c_idx = c_to_idx(s[l])
                s_arr[c_idx] -= 1
                if t_arr[c_idx] > s_arr[c_idx]:
                    satisfied = False
                l += 1
            r += 1
            if r == s_ct or l == s_ct:
                break
            c_idx = c_to_idx(s[r])
            s_arr[c_idx] += 1
            if s_arr[c_idx] >= t_arr[c_idx] and chk():
                satisfied = True
        return s[ans_str[0]:ans_str[1]]
