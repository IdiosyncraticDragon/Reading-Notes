# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 11:37:15 2015

@author: Giancarlo
"""

import numbapro.cudalib.cublas as cublas
import numpy as np
from timeit import default_timer as timer

dim = 10
     # no. of rows/cols


def gemm():
    print("Version 2".center(80, '='))
     
    A = np.random.rand(dim,dim)
    B = np.random.rand(dim, dim)

    D = np.zeros_like(A, order='F')
    
    print("MATRIX A :")
    print A
    print("VECTOR B :")
    print B

    # NumPy
    start = timer()
    E = np.dot(A, B) 
    numpy_time = timer() - start
    print("Numpy took %f seconds" % numpy_time)
    
    # cuBLAS
    blas = cublas.Blas()
    
    start = timer()
    blas.gemm('T', 'T', dim, dim, dim, 1.0, A, B, 1.0, D)
    cuda_time = timer() - start
    print ("RESULT MATRIX EVALUATED WITH CUBLAS")
    print D
    print("CUBLAS took %f seconds" % cuda_time)
    diff = np.abs(D - E)
    print("Maximum error %f" % np.max(diff))


def main():
   
    gemm()

if __name__ == '__main__':
   main()
