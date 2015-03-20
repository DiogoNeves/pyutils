from functools import wraps


def decorator(decorator_func):
    """Turn any function into a decorator.
    Decorators created with this method must have the following arguments:
        fn: Function being decorated
        any function arguments: To pass through to the decorated function

        E.g.:
        @decorator
        def art_decor(fn, *args, **kwargs):
            # do something
            return fn(*args, **kwargs)

        @art_decor
        def my_func(some_string):
            print some_string
    """
    @wraps(decorator_func)
    def new_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return decorator_func(fn, *args, **kwargs)
        return wrapper
    return new_decorator


# To create a decorator with arguments do:
# def outer(arguments):
#     @decorator
#     def real_decorator(fn, *args, **kwargs):
#         do something
#     return real_decorator


def safe_try(exception_types, default_value=None):
    """Wrap try except around a function and return an optional default_value
    if an exception of exception_types is raised."""
    @decorator
    def try_decorator(fn, *args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except exception_types:
            return default_value
    return try_decorator


def wrap_exceptions(exception_types, new_exception_type):
    """Wrap try except around a function and return an optional default_value
    if an exception of exception_types is raised."""
    @decorator
    def try_decorator(fn, *args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except exception_types as ex:
            raise new_exception_type(ex)
    return try_decorator
