class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        
        fleet , last_time = 0 , 0 
        for position , speed in cars:
            time = (target - position) / speed 
            if time > last_time:
                fleet += 1 
                last_time = time
        return fleet
