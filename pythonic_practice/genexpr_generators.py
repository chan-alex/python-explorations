
print("start")

filename = "/var/log/system.log"    # this is a macos specific log file.



def count_seq(seq):
  count=0
  for x in seq:
    count += 1
  return count


# This function uses a generator expressiion.
def count_internet_lines1(fn):
  with open(fn) as infile:
    
      #Using genexpr here saves memory
      internet_lines = (l for l in infile if 'Internet' in l)

      return  count_seq(internet_lines)



    
# This is an object orient equivalent.
# Basically need to define __init__ , __iter__, __next__ special method
class InternetLineFilter:
  def __init__(self, seq):
    self.seq = seq

  def __iter__(self):
    return self

  def __next__(self):
    l = self.seq.readline()

    while l and 'Internet' not in l:
      l = self.seq.readline()

    if not l:
      raise StopIteration

    return l


def count_internet_lines2(fn):
  with open(fn) as infile:

    filter_obj = InternetLineFilter(infile)

    return count_seq(filter_obj)


  
    

# This is a generator.
# The key is the "yield" keyword there.
# The yield return an object that has implements the same special methods as the class
# above.
def filter_internet_lines(seq):
  for l in seq:
    if 'Internet' in l:
      yield l


def count_internet_lines3(fn):
  with open(fn) as infile:

    generator = filter_internet_lines(infile)

    # Can print from the generator
    # for l in generator:
    #   print(l)

    # filter_internet_lines returns an object
    print(generator)

    return count_seq(generator)



