nums = [i for i in range(1, 101)]

target = 54
searches = 0
left = 0
right = len(nums) - 1

while left <= right:
    midpoint = (left + right) // 2
    searches += 1

    if (nums[midpoint] == target):
        print(searches)
        break
    elif (nums[midpoint] > target):
        right = midpoint - 1
    else:
        left = midpoint + 1



