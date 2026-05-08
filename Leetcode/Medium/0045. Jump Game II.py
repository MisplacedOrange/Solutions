class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0
        furthestjump = 0
        currentjump = 0

        for i in range(len(nums) - 1):
            if i + nums[i] > furthestjump:
                furthestjump = i + nums[i]
            if i == currentjump:
                jumps += 1
                currentjump = furthestjump
            if currentjump == len(nums) - 1:
                break
        return jumps
                