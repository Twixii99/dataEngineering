def sum_number_till(n):
    if n == 0:
        return 0

    return n + sum_number_till(n - 1)

print(sum_number_till(100))