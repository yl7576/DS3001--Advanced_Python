from mpi4py import MPI
import sys
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank() 

x = float(sys.argv[1]) 
y = float(sys.argv[2]) 
p_init=1
#bf = np.array([x,y,p_init])

if rank == 0:
    comm.send(p_init*x, dest=1, tag=0)
    p1 = comm.recv(source=1, tag=1)
    comm.send(p1*x, dest=0, tag=2)
    p3 = comm.recv(source=1, tag=3)
    comm.send(p3*x, dest=0, tag=4)
    p5 = comm.recv(source=1, tag=5)
    comm.send(p5*x, dest=0, tag=6)
    p7 = comm.recv(source=1, tag=7)
    comm.send(p7*x, dest=0, tag=8)
    p9 = comm.recv(source=1, tag=9)
    print(p9)
    
else:
    p0 = comm.recv(source=0, tag=0)
    comm.send(p0/y, dest=1, tag = 1)
    p2 = comm.recv(source=0, tag=2)
    comm.send(p2/y, dest=1, tag = 3)
    p4 = comm.recv(source=0, tag=4)
    comm.send(p4/y, dest=1, tag = 5)
    p6 = comm.recv(source=0, tag=6)
    comm.send(p6/y, dest=1, tag = 7)
    p8 = comm.recv(source=0, tag=8)
    comm.send(p8/y, dest=1, tag = 9)
