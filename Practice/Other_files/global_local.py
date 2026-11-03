total = 100

def add(x):
    global total
    total += 11
    return total

print(total)

total = add(11)
print(total)




total = 100

def new_add(x):
    total = 0
    total += 11
    return total

print(total)

total = new_add(11)
print(total)