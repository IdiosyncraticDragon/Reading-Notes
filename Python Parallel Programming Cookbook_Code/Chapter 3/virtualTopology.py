#Virtual Topology– Chapter 3: Process Based Parallelism
from mpi4py import MPI
import numpy as np

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0,0,0,0]
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    grid_rows = int(np.floor(np.sqrt(comm.size)))
    grid_column = comm.size // grid_rows

        
    if grid_rows*grid_column > size:
        grid_column -= 1
    if grid_rows*grid_column > size:
        grid_rows -= 1

    if (rank == 0) :
        print("Building a %d x %d grid topology:"\
              % (grid_rows, grid_column) )
               

#Bidimensional MxN Mesh
##    cartesian_communicator = comm.Create_cart( (grid_rows, grid_column), periods=(False, False), reorder=True)
##    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords( cartesian_communicator.rank ) 

   # print ("rank = %s grid row = %s grid column =%s" %(rank, my_mpi_row, my_mpi_col))


    #Thorus MxN
    cartesian_communicator = \
                           comm.Create_cart( \
                               (grid_rows, grid_column), \
                               periods=(True, True), reorder=True)
    my_mpi_row, my_mpi_col = \
                cartesian_communicator.Get_coords\
                ( cartesian_communicator.rank ) 
##    print ("rank = %s grid row = %s grid column =%s" %(rank, my_mpi_row, my_mpi_col))
##


    neighbour_processes[UP], neighbour_processes[DOWN]\
                             = cartesian_communicator.Shift(0, 1)
    neighbour_processes[LEFT],  \
                               neighbour_processes[RIGHT]  = \
                               cartesian_communicator.Shift(1, 1)
    print ("Process = %s \
row = %s \
column = %s ----> neighbour_processes[UP] = %s \
neighbour_processes[DOWN] = %s \
neighbour_processes[LEFT] =%s neighbour_processes[RIGHT]=%s" \
           %(rank, my_mpi_row, \
             my_mpi_col,neighbour_processes[UP], \
             neighbour_processes[DOWN], \
             neighbour_processes[LEFT] , \
             neighbour_processes[RIGHT]))
 



