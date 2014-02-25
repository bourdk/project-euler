filePath = 'test1'

fp = open(filePath, 'r')

for line in fp:
    a = line.split()
    
    print(a)
