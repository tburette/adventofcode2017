import itertools


def pairwise(l):
    a, b = itertools.tee(l)
    next(b, None)
    return zip(a, b)


with open('day1.txt') as f:
    numbers = f.read()
    # remove trailing \n to keep only numbers
    # appends the first number to the end to handle the looping aspect
    numbers = numbers[:-1] + numbers[0]
    print(sum([int(x) for (x, y) in pairwise(numbers) if x == y]))

    numbers = numbers[:-1]
    print(sum([int(x) for (i, x) in enumerate(numbers) if x == numbers[(i+len(numbers)//2)%len(numbers)]]))
