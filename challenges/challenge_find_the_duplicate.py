def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) < 2:
        return False

    nums.sort()

    for i in range(1, len(nums)):
        if not isinstance(nums[i], int) or nums[i] < 0:
            return False
        if nums[i] == nums[i - 1]:
            return nums[i]

    # teste de outra forma
    # for i in nums:
    #     if not isinstance(i, int) or i < 0:
    #         return False
    #     if i == nums[i - 1]:
    #         return i

    return False
