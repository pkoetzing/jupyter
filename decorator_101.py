"""
How to build a timer-decorator example.

Problem: We have 2 functions 'analyze' and 'optimize'
and temporarily want to extend their behaviour
in order to get their consumed calulation time.
At a later stage we probably want to add a logging,
data caching or authorization mechanism.
We do not want to change all the main programs
where these functions are used.

Run this code in the debugger to understand
how functions and decorators work.
"""

from time import time, sleep

DELAY = 0.01


def analyze():
    """run a quick data analysis"""
    sleep(DELAY)
    print('Analysis finished.')


# 'analyze' points to a function in the global namespace
print(analyze)
analyze()  # execute


def optimize():
    """run a full optimization"""
    sleep(DELAY * 10)
    print('Optimization finished.')


optimize()  # execute


def wrapper():
    """wrapping a timer around analyze only"""
    t0 = time()
    analyze()
    print(f'Analysis took {time() - t0:.3f}s.')


wrapper()  # execute wrapped analyze function


# Redefine 'wrapper' to make it more flexible:
def wrapper(func):
    """wrapper for analyze, optimize and other functions"""
    t0 = time()
    func()
    print(f'Calculation took {time() - t0:.3f}s.')


wrapper(analyze)  # execute wrapped analyze function

# Eventually we want to reassign analyze/optimize
# with their wrapped counterparts, like so:
# analyze = wrapper(analyze)

try:
    print(f'Type of analyze: {type(analyze)}')
    # Just for this demo we do not want to overwrite
    # the original functions (hence the trailing '_')
    analyze_ = wrapper(analyze)
    # Oops, we did not want to have this executed already.
    # Instead this should happen now:
    analyze_()
except TypeError as err:
    print(err)  # Note that we are 'swallowing' the exception here!
    print(f'Type of analyze: {type(analyze_)}')


# Obviously we need a third 'decorator' function
# to achieve the re-assignment.

def decorator(func):
    return wrapper(func)
    # returns function call instead of the function itself
    # but 'return wrapper' doesn't help at all


# So, no surprise this again doesn't work:
try:
    analyze_ = decorator(analyze)
    analyze_()
except TypeError as err:
    print(err)


# Instead we need to put the wrapper inside of the decorator:
def decorator(func):
    # This is the copied definition from above:
    def wrapper(func):
        """flexible wrapper for both analyze and optimize"""
        t0 = time()
        func()
        print(f'Calculation took {time() - t0:.1f}s.')
    return wrapper
    # Now we are actually returning a function.


try:
    analyze_ = decorator(analyze)
    print(analyze_)
    # 'analyze_' now points to a function inside the decorator
    analyze_()
except TypeError as err:
    print(err)
    # But we do not want to call analyze_() with an argument?


# Final solution:
def decorator(func):
    # We do not need to repeat 'func' as a wrapper argument,
    # since the internal function already has access to it.
    def wrapper():
        """flexible wrapper for both analyze and optimize"""
        t0 = time()
        func()
        print(f'Calculation took {time() - t0:.1f}s.')
    return wrapper


analyze = decorator(analyze)
analyze()

optimize = decorator(optimize)
optimize()


# Add "syntactic sugar":
@decorator
def analyze():
    """run a quick data analysis"""
    sleep(DELAY)
    print('Analysis finished.')


analyze()


@decorator
def optimize():
    """run a full optimization"""
    sleep(DELAY * 10)
    print('Optimization finished.')


optimize()


# BONUS: Add an argument and return value:
def decorator(func):
    def wrapper(*args):
        """flexible wrapper for both analyze and optimize"""
        t0 = time()
        func(*args)
        elapsed = time() - t0
        return elapsed
    return wrapper


@decorator
def analyze(delay):
    """run a quick data analysis"""
    sleep(delay)
    print('Analysis finished.')


print(f'Calculation took {analyze(.1):.3f}s.')
