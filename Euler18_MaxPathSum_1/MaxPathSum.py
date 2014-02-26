filePath = 'triangle.txt'

fp = open(filePath, 'r')
nums = [list(map(int, line.split())) for line in fp]
fp.close()

for i in reversed(range(1, len(nums))):
    for j in range(len(nums[i])-1):
        # choose max of 2 children and 'fold' it into the parent
        m = max(nums[i][j], nums[i][j+1])
        nums[i-1][j] += m

print(nums[0][0])
