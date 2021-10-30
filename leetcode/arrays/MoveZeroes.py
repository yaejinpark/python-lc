def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    counter = 0

    #Side note: It's better to do range (0, n) instead of num in nums because
    #I'm changing the array around, which will cause index out of range errors.
    for num in range(0,len(nums)):
        #if number is not 0, move up the non-zero number to the most left it can go to.
        if nums[num] != 0:
            nums[counter] = nums[num]
            counter += 1

    print(counter)
    #The counter should be at 4, len(nums) at 6.
    #Since all non-zero numbers are before index 4, fill the rest with zeros.
    while counter < len(nums):
        nums[counter] = 0
        counter += 1

    print(nums)

numArray = [0,1,0,3,1,2]
moveZeroes(numArray)