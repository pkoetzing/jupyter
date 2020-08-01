my_generator = (i ** 2 for i in range(1_000_000))
sys.getsizeof(my_generator)