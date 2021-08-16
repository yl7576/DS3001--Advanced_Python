import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
N = comm.Get_rank()

value = numpy.zeros(1) 

for r in range(N):
    if r==0:
        print("Process", r, "before receiving has the number", randNum[0])
        comm.Send(value, dest = r+1)
        print("Process",r,"send the value:", value[0], "to process", r+1)
        comm.Recv(value, source = N-1)
        print("Process",r,"receive the value:", value[0], "from process", N-1)
    else:
        comm.Recv(value, source = r-1)
        print("Process",r,"receive the value:", value[0], "from process", r-1)
        value += r^2
        comm.Send(value,dest=r+1)
        print("Process",r,"send the value:", value[0], "to process", r+1)
    
