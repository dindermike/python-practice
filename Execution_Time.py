# Find the duration of a function from start to finish.
import time
from decimal import Decimal, ROUND_HALF_UP

def loop_nums(num_range=5):
    """
    Docstring for loop_nums. Loops through numbers from 1 to the end number passed in as a parameter. Adds the sum of all numbers in the loop.
    
    :param num_range: End range of the loop, must be a positive integer
    :returns: Sum of all numbers in the loop.
    :rtype: int
    :returns: Duration of end_time - start_time
    :rtype: str
    """
    start_time = time.time()
    sum = 0

    for i in range(1, num_range + 1):
        sum = sum + i

    end_time = time.time()

    return sum, str(((end_time - start_time) * 1000) * 1000)
    # Result would otherwise be 0.0000057220458984375 etc...
    # Result now becomes 5.7220458984375 (milliseconds)

user_input = int(input('Enter the number to loop and count: '))

sum, duration = loop_nums(user_input)
print(duration)
duration = Decimal(duration)
duration = duration.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(f"Sum of the function is... {sum}.")
print(f"The duration of the function is... {duration} milliseconds.")

print('--------------------------------------------------')

print('The Docstring of the Custom Function "loop_nums()"...')
print(loop_nums.__doc__)

print('--------------------------------------------------')

# Profile a Function
"""
Will output something that looks like this...
         6 function calls in 8.263 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.263    8.263 <string>:1(<module>)
        1    8.263    8.263    8.263    8.263 Execution_Time.py:5(loop_nums)
        1    0.000    0.000    8.263    8.263 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method time.time}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
import cProfile

print('Profile the Function "loop_nums()"...')
cProfile.run(f'loop_nums({user_input})')