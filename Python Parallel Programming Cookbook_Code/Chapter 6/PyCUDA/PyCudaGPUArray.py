import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
import numpy

a_gpu = gpuarray.to_gpu(numpy.random.randn(5,5).astype(numpy.float32))
a_doubled = (2*a_gpu).get()
print ("ORIGINAL MATRIX")
print a_doubled
print ("DOUBLED MATRIX AFTER PyCUDA EXECUTION USING GPUARRAY CALL")
print a_gpu
