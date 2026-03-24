class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        d=[]
        for i in range(len(nums)):
            if nums[i]==target:
                d.append(i)
        return(d)
        
