def addUp(n):

    sum = 0
    for i in range(n+1):
        sum+=i
    return sum

# print(addUp(100000000))

def addUp(n):
    sum = n*(n+1)//2
    return sum

print(addUp(100000000))