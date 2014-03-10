filePath = 'test1'

with open(filePath) as fp:
    nums = [list(map(int, line.split())) for line in fp]

numsT = [list(i) for i in zip(*nums)]

print(nums)


for i in range(len(nums)):
    for j in range(len(nums[i])):
        r_min = min(nums[i][j + 1:])
        d_min = min(numsT[j][i + 1:])
        r_index = nums[i][j + 1:].index(r_min)
        d_index = numsT[j][i + 1:].index(d_min)







