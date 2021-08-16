import numpy as np
import sys
from math import exp
from mpi4py import MPI

def jk(a_r,k,n,delta):
        res = 0.0
        for i in range(n):
            x = a_r + (i+0.5) * delta
            res += (x**k) * np.exp(-x) * delta
        return res
    
for k in list(range(1, 16)):
    k = int(k)
    
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    local_intg, global_intg = np.zeros(1),np.zeros(1)
    if rank == 0:
        n = np.full(1, 1000, dtype=int) 
    else:
        n = np.zeros(1, dtype=int)
    comm.Bcast(n, root=0)
    
    delta = 1000.0 / (n*size)  
    intg_start = rank * (n*delta)
    local_intg[0] = jk(intg_start, k, n[0], delta)
    
    comm.Reduce(local_intg, global_intg, MPI.SUM, 0)
    if rank == 0:
        print('with k =',k,'integral =', global_intg[0])
