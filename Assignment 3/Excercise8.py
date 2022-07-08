nums = [i for i in range(4, 31)]

even_nums = list(filter(lambda num: num & 1 == 0, nums))
print(even_nums)