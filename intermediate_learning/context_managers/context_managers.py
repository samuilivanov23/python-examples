class ManagedFile:
  def __init__(self, filename):
    self.filename = filename
  
  def __enter__(self):
    print("enter")
    self.file = open(self.filename, 'w')
    return self.file
  
  def __exit__(self, exc_type, exc_value, exc_traceback):
    if self.file:
      self.file.close()
    if exc_type is not None:
      print('Exception has been handled')
    print("exit")
    return True

with ManagedFile("context_managers/notes.txt") as f:
  print("doing stuff...")
  f.write("some todo...")

print("continuing...")
print()

with ManagedFile("context_managers/notes.txt") as f:
  print("doing stuff...")
  f.write("some todo...")
  f.do_something()
print("continuing")


### Implementing a context manager as generator
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
  f = open(filename, 'w')
  try:
    yield f
  finally:
    f.close()

with open_managed_file("context_managers/notes.txt") as f:
  f.write("Some todo from generator CtxMng")