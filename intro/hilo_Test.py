low = 1
high = 1000

# print("Please think of a number between 1 and 1000")
# input("Press ENTER to start")


def guess_binary(answer, low_num, high_num):
    guesses = 1
    while True:
        # print("\tGuessing in the range {} to {}".format(low, high))
        guess = low_num + (high_num - low_num) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct."
        #                  .format(guess)).casefold()

        # if high_low == "h":
        if guess < answer:
            # I have to guess higher.  The low end of the range becomes 1 greater than the guess.
            low_num = guess + 1
        # elif high_low == "l":
        elif guess > answer:
            # I have to guess lower.  The high end of the range becomes 1 less than the guess.
            high_num = guess - 1
        # elif high_low == "c":
        elif guess == answer:
            # print("I got it in {} guesses!".format(guesses))
            # break
            return guesses
        # else:
        #     print("Please enter h, l or c")

        guesses += 1


def factorial(n: int) -> int:
    """Return n! (0! is 1)."""
    return 1 if n == 0 else n * factorial(n-1)


# for number in range(low, high + 1):
#     number_of_guesses = guess_binary(number, low, high)
#     print("{} guessed in {}".format(number, number_of_guesses))
#

# for i in range(36):
#     print(i, factorial(i))