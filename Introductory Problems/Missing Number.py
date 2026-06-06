n = int(input())

sum = n * (n + 1) / 2

nums = [int(i) for i in input().split()]
for num in nums:
    sum -= num

print(int(sum))