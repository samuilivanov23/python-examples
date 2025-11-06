from multiprocessing import Pool

def cube(number):
  return number * number* number

if __name__ == "__main__":
  numbers = range(10)
  p = Pool()
  result = p.map(cube, numbers)
  # result = [p.apply(cube, args=(i,)) for i in numbers]

  p.close()
  p.join()
  print(result)