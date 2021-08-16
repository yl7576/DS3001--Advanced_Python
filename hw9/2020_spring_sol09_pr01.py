import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
status = MPI.Status()

n = 256000

if rank == 0:
    x = np.random.uniform(0,1,n).astype('f').reshape(size, int(n/size))
else:
    x = None

recvbuf = np.empty(int(n/size),dtype='f')
comm.Scatter(x, recvbuf, root=0)
rank_sum = sum(recvbuf)

overall_sum = comm.allreduce(rank_sum, MPI.SUM)
overall_mean = overall_sum/n

#sq_diff = []
#for i in recvbuf:
#    sq_diff.append((i - overall_mean)**2)
rank_sqdiff = sum((i-overall_mean)**2 for i in recvbuf)

std = comm.reduce(rank_sqdiff, MPI.SUM, 0)

if rank==0:
    overall_std = np.sqrt(std/n)
    print('Mean is',overall_mean)
    print('Standard Deviation is', overall_std)
