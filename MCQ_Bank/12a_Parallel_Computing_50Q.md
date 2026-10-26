# Topic 12a: Parallel Computing

**Syllabus:** Parallel virtual machine (PVM) and message passing interface (MPI) libraries and calls, Advanced architectures, Today's fastest computers.

Q1. PVM stands for:
A. Parallel Virtual Memory
B. Parallel Virtual Machine
C. Private Virtual Machine
D. Programmed Virtual Module
Correct Answer: B

Q2. MPI stands for:
A. Message Passing Interface
B. Multiple Processing Integration
C. Memory Passing Interconnect
D. Message Programming Instruction
Correct Answer: A

Q3. Which of the following is a distributed-memory parallel programming standard?
A. OpenMP
B. Pthreads
C. MPI
D. CUDA (only shared-memory view)
Correct Answer: C

Q4. In Flynn's taxonomy, SISD refers to:
A. Single Instruction Single Data
B. Single Instruction Multiple Data
C. Multiple Instruction Single Data
D. Multiple Instruction Multiple Data
Correct Answer: A

Q5. GPUs are best classified as:
A. SISD
B. SIMD
C. MISD
D. SISD and MISD
Correct Answer: B

Q6. Which MPI routine must be called first in every MPI program?
A. MPI_Comm_size
B. MPI_Init
C. MPI_Finalize
D. MPI_Start
Correct Answer: B

Q7. Which MPI routine must be called last to cleanly exit?
A. MPI_Init
B. MPI_Finalize
C. MPI_Abort
D. MPI_Stop
Correct Answer: B

Q8. In MPI, MPI_Comm_rank returns:
A. Total number of processes
B. Rank (ID) of calling process in communicator
C. Processor clock speed
D. Message tag
Correct Answer: B

Q9. In MPI, MPI_Comm_size returns:
A. Rank of process
B. Size of message in bytes
C. Number of processes in communicator
D. Size of communicator buffer
Correct Answer: C

Q10. Default communicator that includes all processes is:
A. MPI_COMM_SELF
B. MPI_COMM_ALL
C. MPI_COMM_WORLD
D. MPI_COMM_NULL
Correct Answer: C

Q11. Which MPI call sends a message (blocking)?
A. MPI_Recv
B. MPI_Send
C. MPI_Bcast
D. MPI_Barrier
Correct Answer: B

Q12. Which MPI call receives a message (blocking)?
A. MPI_Send
B. MPI_Recv
C. MPI_Scatter
D. MPI_Gather
Correct Answer: B

Q13. Non-blocking send in MPI is:
A. MPI_Send
B. MPI_Isend
C. MPI_Ssend
D. MPI_Bsend
Correct Answer: B

Q14. MPI_Bcast is used for:
A. Point-to-point communication
B. One-to-all broadcast within communicator
C. Process termination
D. Mutual exclusion
Correct Answer: B

Q15. MPI_Reduce is used to:
A. Reduce number of processes
B. Combine values from all processes to one root using an operation (e.g., SUM, MAX)
C. Decrease message size
D. Remove deadlock
Correct Answer: B

Q16. MPI_Barrier does:
A. Encrypts messages
B. Synchronizes all processes in a communicator; no process proceeds until all reach it
C. Starts MPI
D. Splits communicator
Correct Answer: B

Q17. MPI_Scatter:
A. Gathers data to root
B. Distributes distinct chunks from root to all processes
C. Broadcasts identical data
D. Scatters processes across nodes
Correct Answer: B

Q18. MPI_Gather:
A. Collects distinct data from all processes to root
B. Sends identical data to all
C. Terminates processes
D. Creates new communicator
Correct Answer: A

Q19. PVM was developed primarily at:
A. Microsoft
B. Oak Ridge National Laboratory / University of Tennessee
C. IBM Zurich
D. IIT Bombay
Correct Answer: B

Q20. Which is TRUE for PVM vs MPI?
A. PVM supports dynamic process spawning and fault tolerance better; MPI is standardized for high performance static SPMD
B. MPI supports only shared memory
C. PVM is only for GPUs
D. MPI cannot do point-to-point
Correct Answer: A

Q21. In PVM, the daemon that must run on each host is called:
A. pvmd
B. mpichd
C. sshd
D. httpd
Correct Answer: A

Q22. PVM function pvm_spawn is used to:
A. Terminate tasks
B. Start new tasks/processes on virtual machine
C. Send mail
D. Allocate shared memory
Correct Answer: B

Q23. PVM function pvm_send / pvm_recv are for:
A. File I/O
B. Message send/receive between tasks
C. Memory allocation
D. Thread creation
Correct Answer: B

Q24. Amdahl's Law gives:
A. Maximum theoretical speedup limited by sequential fraction
B. Minimum memory required
C. Network bandwidth
D. Cache hit ratio
Correct Answer: A

Q25. If 90% of a program is parallelizable, with infinite processors, maximum speedup per Amdahl is:
A. 5x
B. 9x
C. 10x
D. 90x
Correct Answer: C

Q26. Gustafson's Law (scaled speedup) argues:
A. Speedup scales with problem size; parallel portion grows with larger problems
B. Parallel computing is impossible
C. Sequential time always dominates
D. Cache is irrelevant
Correct Answer: A

Q27. Speedup S(p) is defined as:
A. T_parallel / T_serial
B. T_serial / T_parallel
C. T_serial + T_parallel
D. p / T_serial
Correct Answer: B

Q28. Efficiency E(p) is defined as:
A. S(p) / p
B. S(p) * p
C. p / S(p)
D. T(p) / p
Correct Answer: A

Q29. Which is an example of shared-memory API?
A. MPI
B. OpenMP / Pthreads
C. PVM
D. TCP sockets only
Correct Answer: B

Q30. UMA stands for:
A. Uniform Memory Access
B. Unified Message Architecture
C. Universal Multi Agent
D. Uniform Message Passing
Correct Answer: A

Q31. NUMA stands for:
A. Non-Uniform Memory Access
B. New Unified Memory Array
C. Non-Unified Message Application
D. Neutral Memory Access
Correct Answer: A

Q32. In a cluster, nodes are connected via:
A. High-speed interconnect (e.g., InfiniBand, Ethernet)
B. Only dial-up modem
C. Single CPU bus only
D. Printer cable
Correct Answer: A

Q33. Beowulf clusters are built using:
A. Off-the-shelf commodity PCs + open-source software + LAN
B. Only superconductor CPUs
C. Only mainframes
D. Mobile phones only
Correct Answer: A

Q34. Flynn's MIMD includes:
A. Multicore CPUs, clusters, MPPs
B. Only vector processors
C. Only SISD machines
D. Only pipelined CPUs
Correct Answer: A

Q35. SIMD machines include:
A. Vector processors, array processors, GPUs
B. Only MIMD clusters
C. Uniprocessors only
D. Distributed databases only
Correct Answer: A

Q36. Which topology has diameter log2(N) for N nodes?
A. Linear array
B. Hypercube
C. Ring
D. Star (center bottleneck)
Correct Answer: B

Q37. Deadlock in message passing can occur when:
A. Two processes both do blocking Send waiting for matching Recv with no buffering
B. Using MPI_Finalize correctly
C. Using broadcast only
D. Single process program
Correct Answer: A

Q38. MPI_TAG is used to:
A. Identify / filter messages
B. Terminate process
C. Measure time
D. Allocate memory
Correct Answer: A

Q39. MPI_Status object after MPI_Recv contains:
A. Source, tag, error fields
B. Only process rank
C. Only clock speed
D. Compiler version
Correct Answer: A

Q40. Collective communications in MPI require:
A. All processes in communicator to call the routine
B. Only root to call
C. No communicator
D. Only two processes
Correct Answer: A

Q41. Which MPI operation finds maximum value across processes?
A. MPI_Reduce with MPI_MAX
B. MPI_Send with MPI_MAX
C. MPI_Barrier with MPI_MAX
D. MPI_Init with MPI_MAX
Correct Answer: A

Q42. Granularity in parallel computing refers to:
A. Ratio of computation to communication; fine vs coarse grain
B. Size of hard disk
C. Screen resolution
D. Clock frequency only
Correct Answer: A

Q43. Data parallelism means:
A. Same operation on different data partitions across processors
B. Different operations on same data
C. Only task queue
D. Sequential execution
Correct Answer: A

Q44. Task parallelism means:
A. Different tasks/threads execute different operations, possibly on same or different data
B. Same instruction on all data
C. No parallelism
D. Only pipelining in ALU
Correct Answer: A

Q45. Advanced architecture: Multi-core is:
A. Multiple processing cores on single chip sharing/dedicated caches
B. Multiple computers in different countries only
C. Single ALU only
D. Only I/O device
Correct Answer: A

Q46. GPGPU computing commonly uses:
A. CUDA, OpenCL
B. Only COBOL
C. Only HTML
D. Only PVM daemons
Correct Answer: A

Q47. Today's fastest supercomputers (exascale era, e.g., Frontier, Aurora) achieve:
A. ExaFLOPS (~10^18 floating-point ops/sec)
B. Only kiloFLOPS
C. Only megaFLOPS
D. 10 FLOPS
Correct Answer: A

Q48. TOP500 list ranks supercomputers based on:
A. LINPACK benchmark (solving dense linear systems)
B. Number of printers attached
C. Power consumption only
D. Disk capacity only
Correct Answer: A

Q49. Which interconnect is most common in TOP supercomputers for low latency?
A. InfiniBand / proprietary high-speed interconnects (e.g., Slingshot, Tofu)
B. Dial-up 56kbps
C. Bluetooth Low Energy only
D. RS-232 serial
Correct Answer: A

Q50. PVM supports:
A. Heterogeneous network computing - virtual machine hides architecture differences (XDR for data conversion)
B. Only homogeneous Intel machines
C. No network support
D. Only shared memory threads
Correct Answer: A

---
## ANSWER KEY
1-B 2-A 3-C 4-A 5-B 6-B 7-B 8-B 9-C 10-C
11-B 12-B 13-B 14-B 15-B 16-B 17-B 18-A 19-B 20-A
21-A 22-B 23-B 24-A 25-C 26-A 27-B 28-A 29-B 30-A
31-A 32-A 33-A 34-A 35-A 36-B 37-A 38-A 39-A 40-A
41-A 42-A 43-A 44-A 45-A 46-A 47-A 48-A 49-A 50-A
