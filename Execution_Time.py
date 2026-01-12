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