numbah_list = [1,2,4,6]

def even_list_check(number_list):
  even_numbers = []

  for num in number_list:
    if num %2 ==0:
      even_numbers.append(num)
    else:
      pass

  return even_numbers

  return False


even_list_check(numbah_list)