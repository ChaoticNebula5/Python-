def findDuplicate(nums):
    a = nums[0]
    b = nums[0]
    while True:
        a = nums[a]
        b = nums[nums[b]]
        if a == b:
            break
    c = nums[0]
    d = a
    while c != d:
        c = nums[c]
        d = nums[c]
    
    return c

print(findDuplicate(["abcd"]))