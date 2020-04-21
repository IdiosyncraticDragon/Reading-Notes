import pyopencl as cl
from pyopencl import array
import numpy

if __name__ == "__main__":
    vector = numpy.random.randint(100, size=(10 , 1))
    matrix = numpy.random.randint(100, size=(10, 10))

    platform = cl.get_platforms()[0]
    device = platform.get_devices()[0]
    context = cl.Context([device])
    program = cl.Program(context, """
        __kernel void matrix_dot_vector(__global const int *matrix,
        __global const int *vector, __global int *result)
        {
          int gid = get_global_id(0);
          result[gid] = dot(matrix[gid], vector[0]);
        }
        """).build()
    
    queue = cl.CommandQueue(context)
    
    mem_flags = cl.mem_flags
    matrix_buf = cl.Buffer(context, mem_flags.READ_ONLY |   
                 mem_flags.COPY_HOST_PTR, hostbuf=matrix)
    vector_buf = cl.Buffer(context, mem_flags.READ_ONLY |  
                 mem_flags.COPY_HOST_PTR, hostbuf=vector)
    matrix_dot_vector = numpy.zeros(10, numpy.float32)
    destination_buf = cl.Buffer(context, mem_flags.WRITE_ONLY, 
                    matrix_dot_vector.nbytes)
    
    program.matrix_dot_vector(queue, matrix_dot_vector.shape, None,   
                              matrix_buf, vector_buf, destination_buf)
    
    cl.enqueue_copy(queue, matrix_dot_vector, destination_buf)

    print vector
    print matrix
    
    print(matrix_dot_vector)
