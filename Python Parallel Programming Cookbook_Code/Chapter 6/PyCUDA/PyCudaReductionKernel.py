import pycuda.gpuarray as gpuarray
import pycuda.autoinit
import numpy
from pycuda.reduction import ReductionKernel

vector_length = 400

input_vector_a = gpuarray.arange(vector_length, dtype=numpy.int)
input_vector_b = gpuarray.arange(vector_length, dtype=numpy.int)
dot_product = ReductionKernel(numpy.int,
                       arguments="int *x, int *y",
                       map_expr="x[i]*y[i]",
                       reduce_expr="a+b", neutral="0")

dot_product = dot_product(input_vector_a, input_vector_b).get()

print("INPUT MATRIX A")
print input_vector_a

print("INPUT MATRIX B")
print input_vector_b

print("RESULT DOT PRODUCT OF A * B")
print dot_product

