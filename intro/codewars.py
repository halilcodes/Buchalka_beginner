def dig_pow(n, p):
    first = 0
    for i in str(n):
        i = int(i)
        first += i**p
        p +=1
    if first % n == 0:
        return first // n
    else:
        return -1

print(dig_pow(695, 2))

print(1390%695)