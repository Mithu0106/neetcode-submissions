class Solution:
    def merges(self,left,right):
        merge=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                merge.append(left[i])
                i+=1
            else :
                merge.append(right[j])
                j+=1
        merge.extend(left[i:])
        merge.extend(right[j:])
        return merge 

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        return self.merges(left_half , right_half)
