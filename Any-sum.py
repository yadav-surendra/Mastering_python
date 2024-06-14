def anysum (* args):
    sum =0
    for i in range (len(args)):
        sum += args[i]
    return sum
    
print(anysum(1,2,3))

c = anysum(1,2,3,4,5,5)
print(c)
