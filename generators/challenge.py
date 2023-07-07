def odd_num_gen():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds = odd_num_gen()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


piSeries = pi_series()

for i in range(10):
    print(next(piSeries))
