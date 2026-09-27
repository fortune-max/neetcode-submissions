class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from fractions import Fraction
        new_arr = [(pos, spd, idx) for idx, (pos, spd) in enumerate(zip(position, speed))]
        new_arr.sort(reverse=True)
        squad_count, last_car = 1, [*new_arr[0], 0]
        for pos, spd, idx in new_arr[1:]:
            if last_car[1] >= spd:
                squad_count += 1
                last_car = [pos, spd, idx, 0]
            else:
                time = Fraction(pos - last_car[0], last_car[1] - spd)
                c1p = last_car[0] + last_car[1] * time
                c2p = pos + spd * time
                if c1p <= target:
                    last_car[-1] += 1
                else:
                    squad_count += 1
                    last_car = [pos, spd, idx, 0]
        return squad_count
