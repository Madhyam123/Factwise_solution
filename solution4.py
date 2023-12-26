class solution4:
    def index(self,start,target):
        nums2=[1,3,5,6]
        target = 3
        a = len(nums)
        for i in range(len(a)):
            if target == nums[i]:
                return i
        else:
            return nums[i]==target
