filePath = 'test1'

with open(filePath) as fp:
    nums = [list(map(int, line.split())) for line in fp]

numsT = [list(i) for i in zip(*nums)]

print(nums)


for i in range(len(nums)):
    for j in range(len(nums[i])):
        r_min = min(nums[i][j + 1:])
        d_min = min(numsT[j][i + 1:])
        print("r_min: ", r_min)
        print("d_min: ", d_min)
        r_index = nums[i][j + 1:].index(r_min)
        d_index = numsT[j][i + 1:].index(d_min)
        print("r_index: ", r_index)
        print("d_index: ", d_index)

        print("r_min_cost: ", nums[i][r_index:])
        print("d_min_cost: ", numsT[j][d_index:])
#         r_min_cost = sum(nums[j:r_index])
#         d_min_cost = sum(numsT[i:d_index])
#         print(min(r_min_cost, d_min_cost))







