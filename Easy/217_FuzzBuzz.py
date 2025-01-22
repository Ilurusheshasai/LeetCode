## Solution using numpy

import numpy as np

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        numbers = np.arange(1, n + 1)
        result = np.where((numbers % 3 == 0) & (numbers % 5 == 0), 'FizzBuzz',
                 np.where(numbers % 3 == 0, 'Fizz',
                 np.where(numbers % 5 == 0, 'Buzz', numbers.astype(str))))
        return result.tolist()

# When to use it
#  --> When we have larger n value due to vectorized operations