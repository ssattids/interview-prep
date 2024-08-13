class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        naive solution
        time complexity: O(nlogn)
        space complexity: O(nlogn)
        """
        
        # speed = distance/time
        # distance = speed*time
        # time = distance/speed

        # sort by position (such that the largest (closest to the target) is first
        sorted_by_position = sorted(zip(position, speed), key=lambda tup: tup[0])[::-1]
        # keep track of the number of fleets
        fleets = 0
        
        prev_t = -1
        for p, s in sorted_by_position:

            d = target-p 
            t = d / s
            # if the time taken for the next car is going to be larger, then increment the fleet (if it's not going to be larger, it will not be able to pass the car ahead of it and will remain part of the current fleet)
            if t > prev_t:
                fleets += 1
                prev_t = t

        return fleets

