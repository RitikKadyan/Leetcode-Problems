class Solution(object):
    def removeDuplicates(self, nums):
        places_to_remove = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                places_to_remove.append(nums[i])
        for i in range(len(places_to_remove)):
            nums.remove(places_to_remove[i])
        return len(nums)
