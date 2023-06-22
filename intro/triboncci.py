def tribonacci(signature, n):
    sequel = signature
    if n <= 3:
        if len(sequel) == 3:
            return sequel[:n]
        else:
            return sequel
    else:
        new = sum(sequel[-3:])
        sequel.append(new)
        return tribonacci(sequel, n-1)


print(tribonacci([0.5, 0.5, 0.5], 30))
