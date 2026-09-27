class MinStack:

    def __init__(self):
        self.arr = []
        self.curr_min_idx = -1
        self.curr_min_val = float("inf")

    def push(self, val: int) -> None:
        min_if_rm = (self.curr_min_val, self.curr_min_idx)
        if val < self.curr_min_val:
            self.curr_min_idx = len(self.arr)
            self.curr_min_val = val
        self.arr.append((val, min_if_rm))

    def pop(self) -> None:
        last_entry, min_if_rm = self.arr.pop()
        self.curr_min_val = min_if_rm[0]
        self.curr_min_idx = min_if_rm[1]


    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.curr_min_val
