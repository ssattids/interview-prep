class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        BFS solution
        time complexity(O(n))
        space complexity(O(1))
        """

        visited = set({0})
        queue = [0]

        while(queue!=[]):

            index = queue.pop(0)
            visited.add(index)
            if index == len(nums)-1:
                return True

            max_jump_size = nums[index]

            queue = []
            for i in range(1, max_jump_size+1):

                if index + i > len(nums)-1:
                    break

                if index + i not in visited:
                    queue.append(index + i)

        return False