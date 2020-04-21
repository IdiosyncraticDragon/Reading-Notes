#reduction operation – Chapter 3: Process Based Parallelism
import numpy
import numpy as np 
from mpi4py import MPI 
comm = MPI.COMM_WORLD 
size = comm.size 
rank = comm.rank


a_size = 3
recvdata = numpy.zeros(a_size,dtype=numpy.int)
senddata = (rank+1)*numpy.arange(a_size,dtype=numpy.int)

print(" process %s sending %s " %(rank , senddata))


comm.Reduce(senddata,recvdata,root=0,op=MPI.SUM)
print ('on task',rank,'after Reduce:    data = ',recvdata)


