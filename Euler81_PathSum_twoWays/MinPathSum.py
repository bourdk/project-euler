filePath = 'test1'

with open(filePath) as fp:
    nums = [list(map(int, line.split())) for line in fp]

print(nums)

for k in range(len(nums) - 1):
    for i, j in zip(range(len(nums) - 1 - k), reversed(range(1, len(nums[0]) - k))):
        m = min(nums[i][j], nums[i + 1][j - 1])
        nums[i][j - 1] += m

print(nums[0][0])
