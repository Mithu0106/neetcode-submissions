class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxx=[]
        window = nums[:k]
        maxx.append(max(window))
        for r in range(1,len(nums)-k +1):
            window = nums[r:r+k]
            maxx.append(max(window))
        return maxx