'''---------------------------------------------------------------------------------------------------------------------------------------------
Problem Statement : Implement a problem of smallest number with at least n trailing zeroes in factorial.
                    - Given a number n. The task is to find the smallest number whose factorial contains at least n trailing zeroes.
---------------------------------------------------------------------------------------------------------------------------------------------'''


def find_smallest_number_with_trailing_zeros(n):
    def count_trailing_zeros(num):
        count = 0
        while num % 10 == 0:
            count += 1
            num //= 10
        return count

    def factorial_zeros(num):
        zeros = 0
        divisor = 5
        while num >= divisor:
            zeros += num // divisor
            divisor *= 5
        return zeros

    left, right = 0, n * 5  # Set an initial search range
    while left < right:
        mid = (left + right) // 2
        if factorial_zeros(mid) < n:
            left = mid + 1
        else:
            right = mid

    return left

# Example usage:
n = 5
result = find_smallest_number_with_trailing_zeros(n)
print("SmaLlest number with at least", n, "trailing zeros:", result)
