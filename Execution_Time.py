# Find the duration of a function from start to finish.
import time
from decimal import Decimal, ROUND_HALF_UP

def loop_nums(num_range=5):
    start_time = time.time()
    sum = 0

    for i in range(1, num_range + 1):
        sum = sum + i

    end_time = time.time()

    return sum, str(((end_time - start_time) * 1000) * 1000)
    # Result would otherwise be 0.0000057220458984375 etc...

user_input = int(input('Enter the number to loop and count: '))

sum, duration = loop_nums(user_input)
duration = Decimal(duration)
duration = duration.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(f"Sum of the function is... {sum}.")
print(f"The duration of the function is... {duration} milliseconds.")

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

cProfile.run(f'loop_nums({user_input})')