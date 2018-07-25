# TODO make a timeout decorator that will allow for the non-valid ticker serach to timeout
import multiprocessing
from functools import wraps

def timeout(func):
    """
    timeout
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper():

        ####
        # whatever occurs before the function is called
        ####
        func()
        ####
        # whatever occurs after the function is called
        ####


    return wrapper


def just_some_function():
    print("Wheee!")


just_some_function = my_decorator(just_some_function)

just_some_function()

"""
Simple Example of multiprocessing
"""
from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(processes=4) as pool:         # start 4 worker processes
        result = pool.apply_async(f, (10,)) # evaluate "f(10)" asynchronously in a single process
        print(result.get(timeout=1))        # prints "100" unless your computer is *very* slow

        print(pool.map(f, range(10)))       # prints "[0, 1, 4,..., 81]"

        it = pool.imap(f, range(10))
        print(next(it))                     # prints "0"
        print(next(it))                     # prints "1"
        print(it.next(timeout=2))           # prints "4" unless your computer is *very* slow
        for i in range(5000000):
            print(i)



        result = pool.apply_async(time.sleep, (10,))

        print(result.wait(timeout=1))