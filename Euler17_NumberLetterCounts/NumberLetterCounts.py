teens = [0, 6, 6, 8, 8, 7, 7, 9, 8, 8]
ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

total = 0

for i in range(1, 1000):
    # hundreds
    total += ones[i // 100] + ((i // 100) and 1) * 7
    x = i % 100;

    # tens and ones
    if x > 10 and x < 20:    
        total += teens[x % 10]
    else:
        total += tens[x // 10]
        total += ones[x % 10]
        
    # hundred 'and' ...
    if i >= 100 and x != 0:
        total += 3
        
print(total + 11)
    