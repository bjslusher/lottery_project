from time import time as tm


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = tm()
        result = fn(*args, **kwargs)
        t2 = tm()
        print(f"{fn} took {(t2 - t1) / 60} minutes to complete\n")
        return result

    return wrapper



