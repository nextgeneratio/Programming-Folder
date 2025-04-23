class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Pointer for the position of the next valid element
        i = 0
        
        for num in nums:
            # Allow at most two occurrences of each element
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1
        
        return i