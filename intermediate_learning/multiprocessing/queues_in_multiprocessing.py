from multiprocessing import Process, Queue

def square(numbers, quque):
  for i in numbers:
    quque.put(i*i)

def make_negative(numbers, queue):
  for i in numbers:
    queue.put(i*-1)

if __name__ == "__main__":
  print("start main")

  numbers = range(1, 6)
  q = Queue()

  p1 = Process(target=square, args=(numbers, q))
  p2 = Process(target=make_negative, args=(numbers, q))

  p1.start()
  p2.start()
  p1.join()
  p2.join()

  while not q.empty():
    print(q.get())
  
  print("end main")