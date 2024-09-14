class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        stack solution:
        time complexity: O(nlogn) (due to sorting)
        space complexity: O(n)
        """
        sorted_by_position = sorted(zip(position, speed), key=lambda tup: tup[0])[::-1]
                
        stack = []
        for p, s in sorted_by_position:
            #time_to_target =  distance to target / s
            time_to_target = (target-p) / s
            # no matter what, add the new time to target to the stack
            stack.append(time_to_target) 

            # we only want to pop when: 
            # 1) there is more then one element in the stack (more than one element will respresent different fleets) AND
            # 2) the time to target of the "current" car is less than or equal the "previous" car
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)

    
    def carFleetArraySolution(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        naive solution
        time complexity: O(nlogn)
        space complexity: O(n)
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

