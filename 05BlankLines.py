# Calculates the variance of a list of numbers


def calculate_variance(number_list):
  """Returns the variance of the list of numbers."""""
  sum_list = 0
  for number in number_list:
    sum_list += number
  mean = sum_list / len(number_list)

  sum_squares = 0
  for number in number_list:
    sum_squares += (number - mean) ** 2
  variance = sum_squares / len(number_list)
  return variance


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
variance = calculate_variance(num_list)
print("The variance of the list is: " + str(variance))