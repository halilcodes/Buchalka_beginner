fizzbuzz = []

for i in range(1, 31):
    if i % 15 == 0:
        fizzbuzz.append("fizzbuzz")
    elif i % 5 == 0:
        fizzbuzz.append("buzz")
    elif i % 3 == 0:
        fizzbuzz.append("fizz")
    else:
        fizzbuzz.append(str(i))

print(fizzbuzz)
fizzbuzz.clear()

fizzbuzz = ["fizzbuzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else str(i) for i in range(1, 31)]

print(fizzbuzz)
