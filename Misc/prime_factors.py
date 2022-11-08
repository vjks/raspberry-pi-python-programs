def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  list_of_factors = []
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      list_of_factors.append(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return list_of_factors

print(print_prime_factors(100))
# Should print 2,2,5,5