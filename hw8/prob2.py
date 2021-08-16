from mpi4py import MPI
import sys
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank() 

x = float(sys.argv[1]) 
y = float(sys.argv[2]) 
p_init=1
bf = np.array([x,y,p_init])

for i in range(5):
    if rank == 0:
        bf[2]*=bf[0]
        comm.Send(bf, dest=1, tag=0)
        comm.Recv(bf, source = 1, tag = 1)
        if i==4:
            print("final result of p is", bf[2])
    else:
        comm.Recv(bf, source = 0, tag = 0)
        bf[2]/= bf[1]
        comm.Send(bf, dest=0, tag=1)
