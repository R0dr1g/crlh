def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step
    return n
