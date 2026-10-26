# Topic 10: Operating Systems & Unix

**Syllabus:** OS functions, multiprogramming/multiprocessing/multitasking, virtual memory/paging/fragmentation, mutual exclusion/critical regions/lock-unlock, CPU/IO/resource scheduling, deadlock & Banker's, UNIX file system/process/bourne shell/variables/command-line, filters (pr/head/tail/cut/paste/sort/uniq/tr/join/grep/egrep/fgrep/sed/awk), syscalls (create/open/close/read/write/lseek/link/unlink/stat/fstat/umask/chmod/exec/fork/wait/system).

Q1. Operating System primary function is:
A. Resource management and coordination of hardware
B. Only user interface
C. Only memory management
D. Only file handling
Correct Answer: A

Q2. Multiprogramming aims to:
A. Keep CPU busy by having multiple programs in memory
B. Run only one program
C. Reduce memory to zero
D. Increase I/O wait
Correct Answer: A

Q3. Multiprocessing uses:
A. Multiple processors/cores
B. Single processor
C. No CPU
D. Only I/O devices
Correct Answer: A

Q4. Multitasking allows:
A. Multiple tasks to share CPU time
B. One task at a time
C. No task switching
D. Only batch processing
Correct Answer: A

Q5. Virtual memory provides:
A. Illusion of larger main memory than physically available
B. Only disk storage
C. Only faster CPU
D. No memory at all
Correct Answer: A

Q6. Paging divides memory into:
A. Fixed-size blocks called frames/pages
B. Variable-size segments
C. Only one block
D. No blocks
Correct Answer: A

Q7. Fragmentation in memory occurs when:
A. Memory is wasted in small unusable chunks
B. Memory is perfectly organized
C. No memory exists
D. Only disk fragmentation
Correct Answer: A

Q8. Internal fragmentation happens when:
A. Allocated memory is slightly larger than needed
B. Memory is perfectly allocated
C. No memory assigned
D. Only external
Correct Answer: A

Q9. External fragmentation happens when:
A. Free memory is scattered in small blocks
B. Memory is contiguous
C. No free memory
D. Only internal
Correct Answer: A

Q10. Mutual exclusion requires:
A. Only one process accesses critical resource at a time
B. All processes access simultaneously
C. No resource sharing
D. Only one thread
Correct Answer: A

Q11. Critical region is:
A. Section of code accessing shared resources
B. Part of CPU only
C. Memory address only
D. I/O port only
Correct Answer: A

Q12. Lock operation:
A. Acquires a mutex/semaphore
B. Releases a mutex/semaphore
C. Deletes a process
D. Creates a thread
Correct Answer: A

Q13. Unlock operation:
A. Releases a mutex/semaphore
B. Acquires a mutex/semaphore
C. Locks a file
D. Deletes a thread
Correct Answer: A

Q14. CPU scheduling aims to:
A. Maximize CPU utilization and throughput
B. Minimize memory only
C. Only increase I/O
D. Reduce processes to zero
Correct Answer: A

Q15. Shortest Job First (SJF) scheduling:
A. Selects process with smallest burst time
B. Selects first arrived
C. Selects longest
D. Selects random
Correct Answer: A

Q16. Round Robin scheduling uses:
A. Time quantum for each process
B. Priority only
C. First come only
D. Shortest burst
Correct Answer: A

Q17. Priority scheduling may cause:
A. Starvation of low-priority processes
B. No starvation ever
C. Only fast execution
D. CPU idle
Correct Answer: A

Q18. Deadlock occurs when:
A. Processes are blocked waiting for each other
B. CPU is fast
C. Memory is full
D. Only one process
Correct Answer: A

Q19. Necessary conditions for deadlock:
A. Mutual exclusion, hold and wait, no preemption, circular wait
B. Only mutual exclusion
C. Only circular wait
D. Only preemption
Correct Answer: A

Q20. Banker's Algorithm is used for:
A. Deadlock avoidance by checking safe states
B. Deadlock detection only
C. Process creation
D. Memory allocation
Correct Answer: A

Q21. Resource allocation graph is used for:
A. Detecting and avoiding deadlock
B. Only scheduling
C. Only memory
D. Only I/O
Correct Answer: A

Q22. UNIX file system is hierarchical:
A. Tree structure rooted at /
B. Flat structure
C. Circular structure
D. No structure
Correct Answer: A

Q23. In UNIX, everything is treated as:
A. A file
B. Only a directory
C. Only a process
D. Only a device
Correct Answer: A

Q24. Shell is:
A. Command interpreter that mediates between user and OS kernel
B. Part of CPU
C. Only a file
D. A hardware component
Correct Answer: A

Q25. Bourne Shell is:
A. Original UNIX command-line interpreter
B. Windows shell
C. Graphical interface
D. A compiler
Correct Answer: A

Q26. UNIX variable PATH specifies:
A. Directories to search for commands
B. User home directory
C. Current directory only
D. File permissions
Correct Answer: A

Q27. In UNIX, $HOME is a:
A. Shell variable pointing to home directory
B. System error code
C. File name
D. Shell command
Correct Answer: A

Q28. Command-line arguments in UNIX are:
A. Passed to commands/shell scripts
B. Ignored by shell
C. Only for system calls
D. Not used
Correct Answer: A

Q29. UNIX pipe (|) connects:
A. Output of one command to input of another
B. Two files
C. Two users
D. Two CPUs
Correct Answer: A

Q30. UNIX filter processes:
A. Input and produces output
B. Only stores files
C. Only manages processes
D. Only creates users
Correct Answer: A

Q31. pr command in UNIX:
A. Prints file contents
B. Deletes files
C. Copies files
D. Compiles files
Correct Answer: A

Q32. head command in UNIX:
A. Displays first few lines of file
B. Last few lines
C. Middle lines
D. All lines
Correct Answer: A

Q33. tail command in UNIX:
A. Displays last few lines of file
B. First few lines
C. Middle lines
D. All lines
Correct Answer: A

Q34. cut command in UNIX:
A. Extracts columns/fields from lines
B. Combines files
C. Sorts data
D. Deletes files
Correct Answer: A

Q35. paste command in UNIX:
A. Merges lines of files side by side
B. Sorts files
C. Deletes lines
D. Prints only
Correct Answer: A

Q36. sort command in UNIX:
A. Sorts lines of a file
B. Copies files
C. Deletes duplicates
D. Prints heads
Correct Answer: A

Q37. uniq command in UNIX:
A. Filters out repeated adjacent lines
B. Sorts all lines
C. Joins files
D. Translates characters
Correct Answer: A

Q38. tr command in UNIX:
A. Translates or deletes characters
B. Sorts files
C. Cuts columns
D. Prints files
Correct Answer: A

Q39. join command in UNIX:
A. Joins lines of two files on a common field
B. Sorts files
C. Prints lines
D. Deletes lines
Correct Answer: A

Q40. grep command in UNIX:
A. Searches for patterns in files
B. Joins files
C. Sorts lines
D. Deletes files
Correct Answer: A

Q41. egrep is:
A. Extended grep supporting additional regex metacharacters
B. Graphical grep
C. Only searches directories
D. A compiler
Correct Answer: A

Q42. fgrep is:
A. Fixed-string grep (fast pattern matching without regex)
B. File grep
C. Floating grep
D. Fast compiler
Correct Answer: A

Q43. sed is a:
A. Stream editor for filtering/transformation
B. System editor
C. Shell
D. Compiler
Correct Answer: A

Q44. awk is a:
A. Pattern scanning and processing language
B. Shell command
C. File system
D. Compiler
Correct Answer: A

Q45. System call create() is used to:
A. Create a new file
B. Create a directory
C. Create a process
D. Delete a file
Correct Answer: A

Q46. System call open() is used to:
A. Open an existing file
B. Create a file
C. Delete a file
D. Read only
Correct Answer: A

Q47. System call close() is used to:
A. Close an open file descriptor
B. Open a file
C. Create a file
D. Delete a file
Correct Answer: A

Q48. System call read() is used to:
A. Read data from a file descriptor
B. Write data
C. Delete data
D. Close a file
Correct Answer: A

Q49. System call write() is used to:
A. Write data to a file descriptor
B. Read data
C. Close a file
D. Open a file
Correct Answer: A

Q50. System call lseek() is used to:
A. Reposition the file offset
B. Create a file
C. Delete a file
D. Open a file
Correct Answer: A

Q51. System call link() is used to:
A. Create a new directory entry (hard link) for a file
B. Delete a file
C. Copy a file
D. Move a file
Correct Answer: A

Q52. System call unlink() is used to:
A. Remove a directory entry (delete a file)
B. Create a file
C. Link files
D. Open a file
Correct Answer: A

Q53. System call stat() is used to:
A. Get file status/metadata
B. Create a file
C. Delete a file
D. Open a file
Correct Answer: A

Q54. System call fstat() is used to:
A. Get file status from an open file descriptor
B. Create a file
C. Delete a file
D. Close a file
Correct Answer: A

Q55. System call umask() is used to:
A. Set file mode creation mask
B. Set file size
C. Delete a file
D. Read a file
Correct Answer: A

Q56. System call chmod() is used to:
A. Change file permissions
B. Change file owner
C. Change file size
D. Move a file
Correct Answer: A

Q57. System call exec() is used to:
A. Replace current process image with a new program
B. Create a new file
C. Delete a file
D. Copy data
Correct Answer: A

Q58. System call fork() is used to:
A. Create a new child process
B. Delete a process
C. Wait for a process
D. Read a file
Correct Answer: A

Q59. System call wait() is used to:
A. Wait for a child process to terminate
B. Create a process
C. Read a file
D. Write a file
Correct Answer: A

Q60. System call system() is used to:
A. Execute a shell command from a program
B. Create a file
C. Delete a file
D. Copy data
Correct Answer: A

Q61. Process in UNIX is identified by:
A. Process ID (PID)
B. File name
C. User name only
D. Directory name
Correct Answer: A

Q62. Parent process in UNIX:
A. Has a child process
B. Is a kernel thread
C. Is a system call
D. Has no PID
Correct Answer: A

Q63. init process in UNIX has PID:
A. 0 or 1
B. 100
C. 999
D. Any random
Correct Answer: A

Q64. Daemon in UNIX is:
A. Background process running without user interaction
B. Foreground process
C. Shell command
D. System file
Correct Answer: A

Q65. Signal in UNIX is used to:
A. Notify a process of an event
B. Create a file
C. Delete a process
D. Read data
Correct Answer: A

Q66. SIGKILL signal:
A. Terminates a process immediately
B. Stops a process
C. Ignored by process
D. Pauses process
Correct Answer: A

Q67. SIGINT signal:
A. Interrupts a process (e.g., Ctrl+C)
B. Kills a process permanently
C. Ignores a process
D. Creates a process
Correct Answer: A

Q68. Context switch in OS:
A. Saves state of current process and loads state of another
B. Deletes a process
C. Creates a file
D. Reads data
Correct Answer: A

Q69. Process state ready means:
A. Process is waiting to be assigned to CPU
B. Process is running
C. Process is blocked
D. Process is terminated
Correct Answer: A

Q70. Process state blocked means:
A. Process is waiting for an event
B. Process is running
C. Process is ready
D. Process is terminated
Correct Answer: A

Q71. Semaphore is used for:
A. Process synchronization and mutual exclusion
B. Memory allocation
C. File creation
D. CPU scheduling
Correct Answer: A

Q72. Mutex is:
A. Mutual exclusion lock for processes/threads
B. A file type
C. A system call
D. A memory area
Correct Answer: A

Q73. Starvation in OS:
A. A process never gets resources it needs
B. A process runs too fast
C. A process uses too much memory
D. A process is killed
Correct Answer: A

Q74. Thrashing in OS:
A. Excessive paging causing system to spend more time paging than executing
B. Fast CPU execution
C. No memory needed
D. Efficient processing
Correct Answer: A

Q75. Page fault is:
A. An interrupt when a page is not in memory
B. A file system error
C. A CPU error
D. A network error
Correct Answer: A

Q76. TLB (Translation Lookaside Buffer) is:
A. Cache for page table entries
B. A disk cache
C. A CPU register
D. A network buffer
Correct Answer: A

Q77. Demand paging loads a page:
A. Only when it is referenced
B. At process start always
C. At system boot
D. In background always
Correct Answer: A

Q78. Page replacement algorithm FIFO:
A. Replaces the oldest page in memory
B. Replaces the most used
C. Replaces random
D. Replaces next
Correct Answer: A

Q79. Page replacement algorithm LRU:
A. Replaces the least recently used page
B. Replaces oldest
C. Replaces random
D. Replaces most used
Correct Answer: A

Q80. Page replacement algorithm Optimal:
A. Replaces the page that will not be used for longest time
B. Replaces oldest
C. Replaces random
D. Replaces first
Correct Answer: A

Q81. Working set model is used for:
A. Keeping track of pages referenced recently by a process
B. Only memory allocation
C. Only scheduling
D. Only I/O
Correct Answer: A

Q82. Thrashing can be avoided by:
A. Proper page/frame ratio and working set
B. Adding more disk
C. Removing all processes
D. Increasing CPU speed
Correct Answer: A

Q83. Shared memory IPC:
A. Allows processes to share a region of memory
B. Uses only messages
C. Uses only signals
D. Uses only pipes
Correct Answer: A

Q84. Message passing IPC:
A. Processes communicate by sending/receiving messages
B. Shares memory
C. Uses shared files
D. Uses sockets only
Correct Answer: A

Q85. Deadlock detection uses:
A. Resource allocation graphs and cycle detection
B. Only time stamps
C. Only memory
D. Only CPU
Correct Answer: A

Q86. Deadlock recovery can involve:
A. Killing one or more processes
B. Always restarting
C. Only adding memory
D. Only deleting files
Correct Answer: A

Q87. Preemption can resolve deadlock by:
A. Taking resources from a process
B. Killing all processes
C. Ignoring the deadlock
D. Adding more CPU
Correct Answer: A

Q88. Banker's Algorithm requires:
A. Advance knowledge of maximum resource needs
B. No knowledge at all
C. Only current usage
D. Only future requests
Correct Answer: A

Q89. Safe state in Banker's Algorithm means:
A. System can allocate resources without deadlock
B. System is always deadlocked
C. System has no resources
D. System has only one process
Correct Answer: A

Q90. Critical section problem requires:
A. Mutual exclusion, progress, bounded waiting
B. Only mutual exclusion
C. Only progress
D. Only bounded waiting
Correct Answer: A

Q91. Peterson's solution is for:
A. Two-process mutual exclusion
B. Three-process scheduling
C. Memory allocation
D. Deadlock detection
Correct Answer: A

Q92. Test-and-set instruction:
A. Atomically reads and sets a memory location
B. Reads two locations
C. Writes to a file
D. Deletes a variable
Correct Answer: A

Q93. Compare-and-swap instruction:
A. Atomically compares and swaps values
B. Reads and writes files
C. Sends messages
D. Deletes processes
Correct Answer: A

Q94. Semaphores were introduced by:
A. Dijkstra
B. Bellman
C. Turing
D. Kernighan
Correct Answer: A

Q95. Binary semaphore can have values:
A. 0 and 1
B. Any integer
C. Only 0
D. Only 1
Correct Answer: A

Q96. Counting semaphore can have:
A. Non-negative integer values
B. Only 0 or 1
C. Negative values only
D. Only positive
Correct Answer: A

Q97. Bounded buffer problem is also called:
A. Producer-consumer problem
B. Reader-writer problem
C. Dining philosophers
D. Sleeping barber
Correct Answer: A

Q98. Readers-writer problem allows:
A. Multiple readers or one writer
B. Only one reader
C. Multiple writers
D. No readers
Correct Answer: A

Q99. Starvation vs livelock:
A. Starvation is no progress; livelock is active but no useful progress
B. They are the same
C. Starvation is fast execution
D. Livelock uses no CPU
Correct Answer: A

Q100. Belady's anomaly relates to:
A. FIFO page replacement can increase page faults with more frames
B. LRU always works
C. Optimal always fails
D. No anomaly exists
Correct Answer: A

Q101. Swapping moves a process:
A. Between main memory and disk
B. Between CPU and memory
C. Between disk and network
D. Between files
Correct Answer: A

Q102. Virtual address space is:
A. The address space as seen by the process
B. Physical memory address
C. Disk address
D. Network address
Correct Answer: A

Q103. Page table maps:
A. Virtual pages to physical frames
B. Physical to virtual
C. Files to processes
D. Processes to users
Correct Answer: A

Q104. Inverted page table has:
A. One entry per physical frame
B. One entry per process
C. One per user
D. One per file
Correct Answer: A

Q105. Multi-level page table reduces:
A. Size of page table needed by a process
B. CPU speed
C. Disk size
D. Memory size
Correct Answer: A

Q106. Copy-on-write is used in:
A. Forking to share pages until modified
B. Memory allocation
C. File copying
D. Process scheduling
Correct Answer: A

Q107. Memory-mapped files allow:
A. File I/O using memory accesses
B. Only disk I/O
C. Only network I/O
D. Only CPU operations
Correct Answer: A

Q108. TLB miss leads to:
A. Page table walk in memory
B. Page fault always
C. Program crash
D. CPU reset
Correct Answer: A

Q109. Large pages (huge pages) reduce:
A. TLB misses
B. CPU speed
C. Memory size
D. Disk I/O
Correct Answer: A

Q110. Preemptive scheduling:
A. OS forcibly interrupts running process
B. Process voluntarily yields
C. Only batch
D. No preemption possible
Correct Answer: A

Q111. Non-preemptive scheduling:
A. Process keeps CPU until it voluntarily yields or terminates
B. OS interrupts anytime
C. Only priority
D. No scheduling
Correct Answer: A

Q112. Convoy effect occurs when:
A. Short processes wait behind long ones
B. Processes run too fast
C. No waiting
D. Only I/O
Correct Answer: A

Q113. Context switching overhead includes:
A. Saving and restoring registers, PC, PSW
B. Only memory access
C. Only disk access
D. Only network
Correct Answer: A

Q114. CPU burst time is:
A. Amount of time a process spends executing on CPU
B. Amount of time waiting for I/O
C. Amount of memory used
D. Amount of disk access
Correct Answer: A

Q115. I/O burst time is:
A. Amount of time a process spends doing I/O
B. Amount of CPU time
C. Amount of memory
D. Amount of disk space
Correct Answer: A

Q116. Process control block (PCB) contains:
A. Process state, program counter, CPU registers, memory management info
B. Only process name
C. Only memory address
D. Only user ID
Correct Answer: A

Q117. Long-term scheduler selects:
A. Jobs from the job pool to be brought into memory
B. Processes from ready queue
C. Processes from disk
D. Threads only
Correct Answer: A

Q118. Short-term scheduler selects:
A. Process from ready queue to execute on CPU
B. Jobs from pool
C. Processes from disk
D. Threads only
Correct Answer: A

Q119. Throughput is:
A. Number of processes completed per time unit
B. Time to complete one process
C. Time spent waiting
D. Number of processes in ready queue
Correct Answer: A

Q120. Turnaround time is:
A. Total time from submission to completion
B. Time spent in ready queue
C. Time spent in running state only
D. Time spent waiting for I/O
Correct Answer: A

Q121. Waiting time is:
A. Total time a process has been in the ready queue
B. Time spent executing
C. Time spent in I/O
D. Time from creation
Correct Answer: A

Q122. Response time is:
A. Time from submission until first response
B. Time to complete the process
C. Time spent in waiting only
D. Time spent in I/O only
Correct Answer: A

Q123. Preemption occurs when:
A. OS interrupts a running process to schedule another
B. Process voluntarily yields
C. System shuts down
D. Only in batch
Correct Answer: A

Q124. Dispatch latency is:
A. Time to stop one process and start another
B. Time to create a process
C. Time to load a file
D. Time to read memory
Correct Answer: A

Q125. Deterministic scheduling is:
A. All processes have known execution times
B. All processes have random times
C. Only one process
D. Only batch jobs
Correct Answer: A

Q126. Guaranteed scheduling uses:
A. Formula based on fair share of CPU
B. Priority only
C. Round Robin only
D. First come only
Correct Answer: A

Q127. Lottery scheduling uses:
A. Tickets for CPU time allocation
B. Priority only
C. Fixed time slices
D. Random selection
Correct Answer: A

Q128. In UNIX, the file extension is:
A. Not required/meaningful for file type
B. Always .txt
C. Always .sh
D. Always .c
Correct Answer: A

Q129. chmod command changes:
A. File permissions
B. File owner
C. File size
D. File content
Correct Answer: A

Q130. umask sets:
A. Default permissions for newly created files
B. Current directory
C. Shell variable
D. File name
Correct Answer: A

Q131. The /etc/passwd file contains:
A. User account information
B. Passwords in plain text
C. Only usernames
D. Only group names
Correct Answer: A

Q132. The /etc/shadow file stores:
A. Encrypted password information
B. User home directories
C. Shell configuration
D. File permissions
Correct Answer: A

Q133. su command in UNIX:
A. Switch user identity
B. Shut down system
C. Start a service
D. Change directory
Correct Answer: A

Q134. sudo command allows:
A. Execute commands as another user (usually root)
B. Shut down without password
C. Create a new user
D. Delete a file
Correct Answer: A

Q135. cron daemon in UNIX:
A. Schedules periodic execution of commands
B. Manages memory
C. Controls network
D. Handles files
Correct Answer: A

Q136. crontab file contains:
A. Scheduled commands and their timings
B. User passwords
C. File contents
D. Network addresses
Correct Answer: A

Q137. In UNIX, stdin refers to:
A. Standard input (usually keyboard)
B. Standard output
C. Standard error
D. Standard file
Correct Answer: A

Q138. In UNIX, stdout refers to:
A. Standard output (usually screen)
B. Standard input
C. Standard error
D. A file
Correct Answer: A

Q139. In UNIX, stderr refers to:
A. Standard error output
B. Standard input
C. Standard output
D. A device
Correct Answer: A

Q140. The pipe symbol | in UNIX:
A. Connects stdout of one command to stdin of another
B. Creates a file
C. Deletes a file
D. Moves a file
Correct Answer: A

Q141. Redirection operator > in UNIX:
A. Sends output to a file
B. Reads input from a file
C. Appends to a file
D. Prints to screen
Correct Answer: A

Q142. Redirection operator >> in UNIX:
A. Appends output to a file
B. Overwrites a file
C. Reads from a file
D. Deletes a file
Correct Answer: A

Q143. The cat command in UNIX:
A. Concatenates and displays file contents
B. Creates a directory
C. Deletes a file
D. Copies a file
Correct Answer: A

Q144. The more/less command in UNIX:
A. Displays file contents one screen at a time
B. Creates files
C. Deletes files
D. Copies files
Correct Answer: A

Q145. The wc command in UNIX:
A. Counts lines, words, and characters
B. Changes permissions
C. Moves files
D. Finds files
Correct Answer: A

Q146. The who command in UNIX:
A. Displays currently logged-in users
B. Shows file contents
C. Displays processes
D. Shows network connections
Correct Answer: A

Q147. The whoami command in UNIX:
A. Displays current username
B. Displays home directory
C. Displays shell
D. Displays IP address
Correct Answer: A

Q148. The hostname command in UNIX:
A. Displays system hostname
B. Shows current user
C. Shows memory
D. Shows disk space
Correct Answer: A

Q149. The date command in UNIX:
A. Displays current date and time
B. Changes file date
C. Shows system uptime
D. Displays calendar
Correct Answer: A

Q150. The cal command in UNIX:
A. Displays a calendar
B. Shows system time
C. Shows users
D. Shows processes
Correct Answer: A

Q151. The alias command in UNIX:
A. Creates shortcuts for commands
B. Changes file names
C. Sets permissions
D. Creates variables
Correct Answer: A

Q152. The unalias command in UNIX:
A. Removes command aliases
B. Creates new aliases
C. Lists all aliases
D. Resets shell
Correct Answer: A

Q153. The history command in UNIX:
A. Displays command history
B. Shows file contents
C. Shows users
D. Shows memory
Correct Answer: A

Q154. The echo command in UNIX:
A. Displays a line of text
B. Reads a file
C. Deletes a file
D. Copies a file
Correct Answer: A

Q155. The printf command in UNIX:
A. Formats and prints data
B. Creates files
C. Deletes files
D. Changes directories
Correct Answer: A

Q156. The read command in UNIX shell:
A. Reads input from user
B. Prints output
C. Deletes variables
D. Creates files
Correct Answer: A

Q157. In shell scripting, $? contains:
A. Exit status of last command
B. PID of last command
C. Home directory
D. Shell version
Correct Answer: A

Q158. In shell scripting, $$ is:
A. PID of the current shell
B. Exit status
C. Home directory
D. Script name
Correct Answer: A

Q159. In shell scripting, $! is:
A. PID of last background process
B. Exit status
C. Script name
D. Home directory
Correct Answer: A

Q160. In shell scripting, $0 is:
A. Name of the shell script
B. First argument
C. Exit status
D. Home directory
Correct Answer: A

Q161. In shell scripting, $1, $2... refer to:
A. Positional parameters (arguments)
B. Environment variables
C. Shell functions
D. Process IDs
Correct Answer: A

Q162. The test command in shell checks:
A. File attributes and values
B. Network connections
C. CPU usage
D. Memory usage
Correct Answer: A

Q163. The [[ ]] construct in bash is:
A. Extended test command with more features
B. A loop construct
C. A function definition
D. A file operation
Correct Answer: A

Q164. The case statement in shell:
A. Matches patterns and executes corresponding commands
B. A loop
C. A function
D. A variable
Correct Answer: A

Q165. The for loop in shell:
A. Iterates over a list of values
B. Executes conditionally
C. Defines functions
D. Reads files
Correct Answer: A

Q166. The while loop in shell:
A. Executes commands while condition is true
B. Executes once
C. Defines functions
D. Reads user input
Correct Answer: A

Q167. The until loop in shell:
A. Executes commands until condition becomes true
B. Executes forever
C. Defines functions
D. Exits immediately
Correct Answer: A

Q168. The break command in shell:
A. Exits a loop
B. Defines a function
C. Reads input
D. Creates files
Correct Answer: A

Q169. The continue command in shell:
A. Skips to next iteration of a loop
B. Exits the shell
C. Deletes a file
D. Prints output
Correct Answer: A

Q170. A shell function is defined with:
A. function_name() { ... }
B. def function_name():
C. func function_name()
D. create function_name()
Correct Answer: A

Q171. The source/dot command in shell:
A. Executes commands from a file in current shell
B. Runs a script in subshell
C. Compiles a file
D. Creates a file
Correct Answer: A

Q172. Here document in shell uses:
A. << to redirect input until a delimiter
B. A for loop
C. A while condition
D. A function call
Correct Answer: A

Q173. The trap command in shell:
A. Catches signals and executes commands
B. Creates traps
C. Deletes files
D. Compiles code
Correct Answer: A

Q174. The getopts command in shell:
A. Parses command-line options
B. Gets process options
C. Reads files
D. Displays help
Correct Answer: A

Q175. The shift command in shell:
A. Shifts positional parameters
B. Moves files
C. Changes directory
D. Deletes variables
Correct Answer: A

Q176. In shell, export makes a variable:
A. Available to child processes
B. Available only in current script
C. Temporary
D. System-wide
Correct Answer: A

Q177. The type command in shell:
A. Shows how a command is interpreted
B. Changes file type
C. Shows file contents
D. Lists users
Correct Answer: A

Q178. The which command in shell:
A. Finds the path of a command
B. Displays help
C. Shows history
D. Lists files
Correct Answer: A

Q179. The find command in UNIX:
A. Searches for files based on criteria
B. Compiles programs
C. Deletes processes
D. Shows users
Correct Answer: A

Q180. The locate command in UNIX:
A. Quickly finds files using a database
B. Searches memory
C. Shows network
D. Displays time
Correct Answer: A

Q181. The grep -r option:
A. Recursively searches directories
B. Reverses search
C. Counts lines
D. Shows file size
Correct Answer: A

Q182. The tar command in UNIX:
A. Archives files (tape archive)
B. Compiles programs
C. Deletes files
D. Shows disk space
Correct Answer: A

Q183. The gzip command in UNIX:
A. Compresses files
B. Decompresses files
C. Both A and depends on mode
D. Only archives
Correct Answer: C

Q184. The bzip2 command:
A. Compresses files with better compression than gzip
B. Only archives
C. Only decompresses
D. Only extracts
Correct Answer: A

Q185. The zip command in UNIX:
A. Creates zip archives
B. Only compresses
C. Only extracts
D. Only lists
Correct Answer: A

Q186. The chmod symbolic mode u+x means:
A. Adds execute permission for owner
B. Removes write permission
C. Adds read for group
D. Removes all permissions
Correct Answer: A

Q187. The chown command changes:
A. File owner and/or group
B. File permissions
C. File content
D. File name
Correct Answer: A

Q188. The ln command creates:
A. Links (hard or symbolic)
B. Files
C. Directories only
D. User accounts
Correct Answer: A

Q189. A symbolic link (soft link) in UNIX:
A. Points to the path of another file
B. Is an exact copy of the file
C. Is a hard link
D. Is a directory
Correct Answer: A

Q190. A hard link in UNIX:
A. Shares the same inode as the original file
B. Points to file path
C. Is a copy of the file
D. Is a symbolic link
Correct Answer: A

Q191. The dd command in UNIX:
A. Converts and copies files
B. Deletes files
C. Compiles programs
D. Shows users
Correct Answer: A

Q192. The diff command in UNIX:
A. Compares files line by line
B. Deletes files
C. Compiles programs
D. Shows processes
Correct Answer: A

Q193. The patch command in UNIX:
A. Applies differences to files
B. Creates patches
C. Deletes files
D. Compiles files
Correct Answer: A

Q194. The split command in UNIX:
A. Splits a file into smaller parts
B. Joins files
C. Deletes files
D. Compiles files
Correct Answer: A

Q195. The tee command in UNIX:
A. Reads from stdin and writes to stdout and files
B. Deletes files
C. Compiles code
D. Shows history
Correct Answer: A

Q196. The xargs command in UNIX:
A. Builds and executes command lines from stdin
B. Deletes files
C. Compiles programs
D. Shows users
Correct Answer: A

Q197. The screen command in UNIX:
A. Allows multiple terminal sessions
B. Deletes files
C. Compiles programs
D. Shows users
Correct Answer: A

Q198. The tmux command in UNIX:
A. Terminal multiplexer for multiple sessions
B. File manager
C. Compiler
D. Shell script
Correct Answer: A

Q199. The sort -r option in UNIX:
A. Sorts in reverse order
B. Sorts numerically
C. Sorts by file size
D. Sorts by date
Correct Answer: A

Q200. The uniq -c option:
A. Counts repeated lines
B. Removes duplicates only
C. Sorts lines
D. Joins files
Correct Answer: A

---
## ANSWER KEY
1-A 2-A 3-A 4-A 5-A 6-A 7-A 8-A 9-A 10-A
11-A 12-A 13-A 14-A 15-A 16-A 17-A 18-A 19-A 20-A
21-A 22-A 23-A 24-A 25-A 26-A 27-A 28-A 29-A 30-A
31-A 32-A 33-A 34-A 35-A 36-A 37-A 38-A 39-A 40-A
41-A 42-A 43-A 44-A 45-A 46-A 47-A 48-A 49-A 50-A
51-A 52-A 53-A 54-A 55-A 56-A 57-A 58-A 59-A 60-A
61-A 62-A 63-A 64-A 65-A 66-A 67-A 68-A 69-A 70-A
71-A 72-A 73-A 74-A 75-A 76-A 77-A 78-A 79-A 80-A
81-A 82-A 83-A 84-A 85-A 86-A 87-A 88-A 89-A 90-A
91-A 92-A 93-A 94-A 95-A 96-A 97-A 98-A 99-A 100-A
101-A 102-A 103-A 104-A 105-A 106-A 107-A 108-A 109-A 110-A
111-A 112-A 113-A 114-A 115-A 116-A 117-A 118-A 119-A 120-A
121-A 122-A 123-A 124-A 125-A 126-A 127-A 128-A 129-A 130-A
131-A 132-A 133-A 134-A 135-A 136-A 137-A 138-A 139-A 140-A
141-A 142-A 143-A 144-A 145-A 146-A 147-A 148-A 149-A 150-A
151-A 152-A 153-A 154-A 155-A 156-A 157-A 158-A 159-A 160-A
161-A 162-A 163-A 164-A 165-A 166-A 167-A 168-A 169-A 170-A
171-A 172-A 173-A 174-A 175-A 176-A 177-A 178-A 179-A 180-A
181-A 182-A 183-C 184-A 185-A 186-A 187-A 188-A 189-A 190-A
191-A 192-A 193-A 194-A 195-A 196-A 197-A 198-A 199-A 200-A