from threading import Thread

def square_numbers():
  for i in range(1000):
    result = i * i

if __name__ == "__main__":
  threads = []
  num_threads = 10

  # create threads and assign a fun to each thread
  for i in range(num_threads):
    thread = Thread(target=square_numbers)
    threads.append(thread)
  
  # start all threads
  for thread in threads:
    thread.start()
  
  # wait for all the threads to finish
  # Block the main thread until then
  for thread in threads:
    thread.join()