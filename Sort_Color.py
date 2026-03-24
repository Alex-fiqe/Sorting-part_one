class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            k = i
            for j in range(i,len(nums)):
                if nums[k]>nums[j]:
                    k = j
            temp=nums[i]
            nums[i]=nums[k]
            nums[k]=temp
        return nums   
