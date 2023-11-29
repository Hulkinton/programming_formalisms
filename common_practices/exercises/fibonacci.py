def fibonacci(length, start_at_1=False):
    """returns a fibonacci sequence of specified length, starting at 0 or 1"""
    if start_at_1:
        start = [1,1]
    else:
        start = [0,1]
    for index in range(length):
        if index == 0:
            sequence = [start[0]]
        else:
            if index == 1:
                element = start[1]
            else:
                element = sequence[index-1] + sequence[index-2]
            sequence = sequence+[element]
    return sequence
#
assert fibonacci(1) == [0]

assert fibonacci(2) == [0,1]

assert fibonacci(3) == [0,1,1]

assert fibonacci(3, True) == [1,1,2]

