class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums
    
    def quicksort(self, nums, lower, upper):
        if lower < upper:
            pivot = self.partition(nums, lower, upper)
            self.quicksort(nums, lower, pivot - 1)
            self.quicksort(nums, pivot + 1, upper)
        else:
            return
        
    def partition(self, nums, lower, upper):
        
        pivot = nums[upper]
        
        i = lower
        
        for j in range(lower, upper):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                
        nums[i], nums[upper] = nums[upper], nums[i]
        
        return i