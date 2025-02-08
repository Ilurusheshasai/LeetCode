#Solved it using Sieve of Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Use boolean array to save memory
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
                # Only mark multiples starting from i*i
                for j in range(i*i, n, i):
                    is_prime[j] = False

        return count