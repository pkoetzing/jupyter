# Decorator Excercises

**Use case:** Your colleagues published a new package on Nexus with
a sophisticated _analyze_ function. You want to use this functions, but unfortunatly you need additional features. You could either

- Make a copy of that function from the repo and change it to your needs. However, you won't benefit from future improvements then.
- Write a new function that calls _analyze_, but does your specific pre- and postprocessing before and after.
If you're lucky you can apply this "wrapper" on other functions in the package too.

Given is a simple _'analyze'_ function

```python
import time

def analyze():
    delay = 1
    time.sleep(delay)
```

1. Wrap this function with an execution timer using time.time()
that prints the seconds used:  
start timer - call analyze - stop timer - print elapsed)

1. Reassign the wrapper to the original function (aka. _'decorate it'_)

1. Make the _delay_ an argument to _analyze_.

1. Return the time used from the decorated function.

1. If you get stuck, open _decorator_101.py_ and run the code
in a debugger to analyze it.

Note: The **@decorate** syntax is not needed for this,
but a solid understanding of how functions work in Python :wink:
