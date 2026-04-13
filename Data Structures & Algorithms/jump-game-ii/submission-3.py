class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest_point = 0
        threshhold = 0
        for i in range(len(nums)-1):
            farthest_point = max(i + nums[i], farthest_point)
            if (i == threshhold):
                jumps += 1
                threshhold = farthest_point
        return jumps