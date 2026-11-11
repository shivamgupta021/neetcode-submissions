class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = dict(zip(position, speed))
        fleets = 0
        fleet_time = 0

        for pos, spd in sorted(cars.items(), reverse=True):
            time = (target - pos) / spd
            if time > fleet_time:
                fleets += 1
                fleet_time = time

        return fleets