from multiprocessing import Process
import os

def square_numbers():
  for i in range(1000):
    result = i * i

if __name__ == "__main__":
  processes = []
  num_processes = os.cpu_count()

  for i in range(num_processes):
    process = Process(target=square_numbers)
    processes.append(process)
  
  for process in processes:
    process.start()
  
  for process in processes:
    process.join()