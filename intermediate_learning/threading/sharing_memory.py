from threading import Thread, Lock
import time

database_value = 0

def increase(lock):
  global database_value

  with lock:
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy

if __name__ == "__main__":
  lock = Lock()

  print("Start value: ", database_value)
  t1 = Thread(target=increase, args=(lock,)) # the comma is needed here because args receives a tuple
  t2 = Thread(target=increase, args=(lock,))
  t1.start()
  t2.start()
  t1.join()
  t2.join()
  print("End value: ", database_value)

  print("end main function")