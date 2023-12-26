class Solution2:
    result = 1
    length = nums.len()
    if(length==0):
        return 0
    temp = nums[0]
    for i in range(nums):
        cur = nums[i]
        if(temp!=cur):
            nums[result]=cur
            temp=cur
return result
