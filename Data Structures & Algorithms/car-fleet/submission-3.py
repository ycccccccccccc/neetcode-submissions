class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = len(position)
        cars = [(position[i], speed[i]) for i in range(l)]
        cars.sort()
        
        fleet = 1
        last_car = l-1
        periods = [(target-cars[i][0])/cars[i][1] for i in range(l)]
        for i in range(l-2, -1, -1):
            if periods[i] > periods[last_car]:
                fleet += 1
                last_car = i
        return fleet