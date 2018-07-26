import multiprocessing.pool
import functools


def timeout(max_timeout=20):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""

        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            try:
                return async_result.get(max_timeout)
            except multiprocessing.context.TimeoutError:
                pool.close()
                print('Timeout limit exceeded')

        return func_wrapper
    return timeout_decorator


def handler(my_function):

    def wrapper(*args, **kwargs):

        try:
            return my_function(*args, **kwargs)
        except AttributeError:
            pass
    return wrapper