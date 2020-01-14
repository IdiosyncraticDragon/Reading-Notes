from pycsp.parallel import *

@process
def processCounter(cout, limit):
  for i in xrange(limit):
    cout(i)
  poison(cout)

@process
def processPrinter(cin):
  while True:
    print cin(),

A = Channel('A')
Parallel(
  processCounter(A.writer(), limit=5),
  processPrinter(A.reader())
)

shutdown()
