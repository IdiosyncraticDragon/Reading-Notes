import pyopencl as cl
from pyopencl import array
import numpy as np

if __name__ == "__main__":
    vector = np.random.randint(vector_dimension, size=vector_dimension)
    matrix = np.random.randint(vector_dimension, size=((vector_dimension,vector_dimension))
    
##   """
##    vector = numpy.zeros((1, 1), cl.array.vec.float4)
##    matrix = numpy.zeros((1, 4), cl.array.vec.float4)
##    matrix[0, 0] = (1, 2, 4, 8)
##    matrix[0, 1] = (16, 32, 64, 128)
##    matrix[0, 2] = (3, 6, 9, 12)
##    matrix[0, 3] = (5, 10, 15, 25)
##    vector[0, 0] = (1, 2, 4, 8)
##    """
##   
####    platform = cl.get_platforms()[0]
####    device = platform.get_devices()[0]
####    context = cl.Context([device])
####    program = cl.Program(context, """
####        __kernel void matrix_dot_vector(__global const float4 *matrix,
####        __global const float4 *vector, __global float *result)
####        {
####          int gid = get_global_id(0);
####          result[gid] = dot(matrix[gid], vector[0]);
####        }
####        """).build()
####    
####    queue = cl.CommandQueue(context)
####    
####    mem_flags = cl.mem_flags
####    matrix_buf = cl.Buffer(context, mem_flags.READ_ONLY |   
####                 mem_flags.COPY_HOST_PTR, hostbuf=matrix)
####    vector_buf = cl.Buffer(context, mem_flags.READ_ONLY |  
####                 mem_flags.COPY_HOST_PTR, hostbuf=vector)
####    matrix_dot_vector = numpy.zeros(4, numpy.float32)
####    destination_buf = cl.Buffer(context, mem_flags.WRITE_ONLY, 
####                    matrix_dot_vector.nbytes)
####    
####    program.matrix_dot_vector(queue, matrix_dot_vector.shape, None,   
####                              matrix_buf, vector_buf, destination_buf)
####    
####    cl.enqueue_copy(queue, matrix_dot_vector, destination_buf)
####    
####    print(matrix_dot_vector)
