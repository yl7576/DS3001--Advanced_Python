from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank() 

x=2
y=4
p_init=1

if rank == 0:
    comm.send(p_init*x, dest=1, tag=0)
    p1 = comm.recv(source=1, tag=1)
    print(p1)
    
elif rank == 1:
    p0 = comm.recv(source=0, tag=0)
    comm.send(p0/y, dest=1, tag = 1)
