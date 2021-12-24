class Solution:
    def kthLargestNumber(self, nums, k):
        container = []
        for i in range(len(nums)):
            container.append(int(nums[i]))

        container.sort()
        return str(container[-k])



s = Solution()
print(s.kthLargestNumber(["2","21","12","1"], 3))