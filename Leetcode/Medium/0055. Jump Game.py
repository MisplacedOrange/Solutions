class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] >= len(nums) - 1:
            return True
        furthestjump = 0
        currentjump = 0
        possible = False

        for i in range(len(nums) - 1):
            if i + nums[i] > furthestjump:
                furthestjump = i + nums[i]
            if i == currentjump:
                currentjump = furthestjump
            if currentjump >= len(nums):
                break
        if currentjump >= len(nums) - 1:
            possible = True
        return possible
        
        