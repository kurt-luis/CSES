n = int(input())
nums = [int(i) for i in input().split()]

moves = 0
for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        moves += nums[i - 1] - nums[i]
        nums[i] = nums[i - 1]

print(moves)