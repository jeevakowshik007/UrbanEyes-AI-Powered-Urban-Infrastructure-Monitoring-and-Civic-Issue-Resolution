# Topic 5: Computer Organization

**Syllabus:** Machine instructions and addressing modes, ALU, data path and control unit, Instruction pipelining, pipeline hazards, Memory hierarchy: cache, main memory and secondary storage; I/O interface (interrupt and DMA mode).

Q1. Which addressing mode uses PC-relative offset for branch target?
A. Immediate
B. Direct
C. Relative
D. Indirect
Correct Answer: C

Q2. In zero-address machine, operands are stored in?
A. Registers
B. Stack
C. Memory
D. Cache
Correct Answer: B

Q3. Opcode length n bits allows maximum how many distinct operations?
A. n
B. 2n
C. 2^n
D. n^2
Correct Answer: C

Q4. Which addressing mode is best for array traversal with auto-increment?
A. Immediate
B. Auto-increment
C. Relative
D. Implicit
Correct Answer: B

Q5. MOV R1, (R2) is an example of?
A. Register
B. Register-indirect
C. Direct
D. Immediate
Correct Answer: B

Q6. Effective address in indexed addressing is?
A. PC+offset
B. Index+base
C. Register content
D. Immediate value
Correct Answer: B

Q7. Stack addressing for ADD implicitly uses?
A. TOS+next
B. PC
C. MAR
D. IR
Correct Answer: B

Q8. Immediate addressing is suitable for?
A. Constants
B. Pointers
C. Arrays
D. Subroutines
Correct Answer: A

Q9. Number of address fields in three-address instruction for A=B+C?
A. 1
B. 2
C. 3
D. 4
Correct Answer: C

Q10. Indirect addressing requires how many memory accesses minimum?
A. 0
B. 1
C. 2
D. 3
Correct Answer: C

Q11. Base-register addressing is used for?
A. Relocation
B. Constants
C. Stack
D. I/O
Correct Answer: A

Q12. Which mode supports position-independent code?
A. Absolute
B. PC-relative
C. Indirect
D. Immediate
Correct Answer: B

Q13. Accumulator machine uses how many addresses?
A. 0
B. 1
C. 2
D. 3
Correct Answer: A

Q14. In RISC, addressing modes are typically?
A. Many
B. Few and simple
C. Microcoded
D. Variable
Correct Answer: B

Q15. Displacement = base 1000 + offset 250 gives EA?
A. 750
B. 1000
C. 1250
D. 250000
Correct Answer: A

Q16. Register-indirect saves what compared to direct?
A. Bits
B. Time
C. Power
D. Nothing
Correct Answer: B

Q17. Immediate field in MIPS I-type is how many bits?
A. 5
B. 16
C. 26
D. 32
Correct Answer: A

Q18. J-type instruction is used for?
A. ALU
B. Jump
C. Load
D. Branch conditional
Correct Answer: B

Q19. Big-endian stores MSB at?
A. Highest address
B. Lowest address
C. Middle
D. Register
Correct Answer: A

Q20. Little-endian example processor?
A. IBM 370
B. Intel x86
C. Motorola 68000
D. SPARC
Correct Answer: B

Q21. Stack overflow occurs when?
A. POP empty
B. PUSH full
C. ADD zero
D. JMP fail
Correct Answer: B

Q22. Which instruction changes PC conditionally?
A. MOV
B. Branch
C. ADD
D. NOP
Correct Answer: B

Q23. Addressing mode of loop counter update is often?
A. Register
B. Immediate
C. Indirect
D. Relative
Correct Answer: A

Q24. Memory-indirect vs cache: extra access causes?
A. Speedup
B. Penalty
C. Hit
D. Coherence
Correct Answer: C

Q25. Auto-decrement is used for?
A. Stack push
B. Queue
C. Heap
D. Array read
Correct Answer: B

Q26. `LOAD M[X]` where X is address of address is?
A. Direct
B. Indirect
C. Immediate
D. Indexed
Correct Answer: B

Q27. Which is not an addressing mode?
A. Implied
B. Paging
C. Indexed
D. Autoincrement
Correct Answer: B

Q28. Instruction format contains?
A. Opcode+operands
B. Data only
C. Control only
D. Clock
Correct Answer: A

Q29. Fixed-length instructions simplify?
A. Decoding
B. Storage
C. Pipelining both fetch/decode
D. All
Correct Answer: C

Q30. Variable-length instruction example ISA?
A. MIPS
B. RISC-V
C. x86
D. ARM fixed
Correct Answer: C

Q31. Effective address of `ADD #5,R1` source is?
A. R1
B. 5 itself
C. M[5]
D. PC
Correct Answer: B

Q32. Post-indexed addressing updates register?
A. Before use
B. After use
C. Never
D. On interrupt
Correct Answer: B

Q33. Which mode needs no EA calculation?
A. Immediate
B. Indexed
C. Based
D. Indirect
Correct Answer: A

Q34. Stack machine expression A+B requires?
A. PUSH A,PUSH B,ADD
B. ADD A,B
C. LOAD both
D. MOV
Correct Answer: A

Q35. One-address instruction needs implicit?
A. Accumulator
B. Cache
C. Bus
D. ALU flag
Correct Answer: B

Q36. Two-address `ADD R1,R2` means?
A. R1=R1+R2
B. R2=R1+R2
C. R1=R2
D. MEM=R1+R2
Correct Answer: A

Q37. Endianness affects?
A. ALU speed
B. Byte order
C. Clock
D. Opcode
Correct Answer: B

Q38. Alignment requirement improves?
A. Memory bandwidth
B. Power
C. Code size
D. Interrupts
Correct Answer: B

Q39. Unaligned access may cause?
A. Extra cycles/trap
B. Faster
C. No effect
D. Halt always
Correct Answer: A

Q40. Instruction cycle order is?
A. Decode-fetch-execute
B. Fetch-decode-execute
C. Execute-fetch-decode
D. Fetch-execute-decode
Correct Answer: B

Q41. PC holds?
A. Next instruction addr
B. Current data
C. Opcode
D. Flag
Correct Answer: A

Q42. IR holds?
A. Current instruction
B. Next address
C. Data
D. Status
Correct Answer: A

Q43. MAR holds?
A. Address for memory access
B. Data
C. Instruction
D. Flag
Correct Answer: A

Q44. MDR holds?
A. Data to/from memory
B. Address
C. PC
D. Opcode
Correct Answer: A

Q45. Expanding opcode allows?
A. Variable op lengths
B. Fixed ops
C. No operands
D. Larger memory
Correct Answer: A

Q46. `BEQ offset` uses which mode?
A. PC-relative
B. Absolute
C. Indirect
D. Stack
Correct Answer: A

Q47. Register file with 32 regs needs bits per specifier?
A. 3
B. 4
C. 5
D. 6
Correct Answer: B

Q48. Memory address 16-bit, word-addressable, max words?
A. 16K
B. 32K
C. 64K
D. 1M
Correct Answer: C

Q49. Byte-addressable 24-bit address space size?
A. 16MB
B. 8MB
C. 4MB
D. 2MB
Correct Answer: A

Q50. Which supports subroutine linkage best?
A. Implied
B. Register-indirect + stack
C. Immediate
D. Direct only
Correct Answer: B

Q51. ALU performs?
A. Arithmetic/logic
B. Control sequencing
C. I/O transfer
D. Decoding
Correct Answer: A

Q52. Control unit function is?
A. Execute ALU
B. Generate control signals
C. Store data
D. Fetch operands only
Correct Answer: B

Q53. Hardwired control is?
A. Slow flexible
B. Fast inflexible
C. Microprogrammed
D. Software
Correct Answer: B

Q54. Microprogrammed control uses?
A. Control memory
B. PLA only
C. Random logic
D. Cache
Correct Answer: A

Q55. Datapath includes?
A. ALU+regs+buses
B. Only memory
C. Only CU
D. I/O devices
Correct Answer: A

Q56. Single-bus organization bottleneck is?
A. Bus contention
B. ALU speed
C. Clock
D. Memory size
Correct Answer: A

Q57. Three-bus datapath allows?
A. Parallel operand fetch
B. Slower
C. Serial only
D. No pipelining
Correct Answer: A

Q58. Register transfer `R1<-[R2]+[R3]` needs ALU op?
A. ADD
B. SUB
C. AND
D. OR
Correct Answer: A

Q59. Flags Z,N,C,V are set by?
A. CU
B. ALU outcome
C. Memory
D. Bus
Correct Answer: B

Q60. Carry flag indicates?
A. Zero
B. Unsigned overflow
C. Sign
D. Parity
Correct Answer: B

Q61. Overflow flag indicates?
A. Signed overflow
B. Zero
C. Carry
D. Interrupt
Correct Answer: A

Q62. Shifter in datapath does?
A. Multiply only
B. Shift/rotate
C. Add
D. Store
Correct Answer: B

Q63. Single-cycle datapath CPI is?
A. 1
B. >1 variable
C. <1
D. 0
Correct Answer: A

Q64. Multi-cycle datapath advantage?
A. Shorter cycle, resource sharing
B. Higher CPI always bad
C. No control
D. Larger clock only
Correct Answer: B

Q65. Pipelining improves?
A. Latency
B. Throughput
C. Clock period
D. Code size
Correct Answer: B

Q66. 5-stage MIPS pipeline stages order?
A. IF-ID-EX-MEM-WB
B. ID-IF-EX-MEM-WB
C. IF-EX-ID-MEM-WB
D. FE-DE-ME-WB
Correct Answer: A

Q67. Pipeline speedup ideal with k stages?
A. k
B. 1/k
C. k^2
D. log k
Correct Answer: B

Q68. Data hazard occurs due to?
A. Branch
B. Data dependency
C. Structural
D. Control signal
Correct Answer: B

Q69. RAW hazard example?
A. ADD R1,R2; SUB R3,R1
B. Two loads same cycle
C. Branch mispredict
D. Cache miss
Correct Answer: A

Q70. WAR hazard occurs in?
A. In-order 5-stage
B. Out-of-order
C. Single-cycle
D. Unpipelined
Correct Answer: B

Q71. Structural hazard is due to?
A. Resource conflict
B. Data dependency
C. Branch
D. Interrupt
Correct Answer: A

Q72. Control hazard is due to?
A. Branch/jump
B. ALU delay
C. Memory conflict
D. Register file
Correct Answer: A

Q73. Data forwarding resolves?
A. Structural
B. Data hazard stall
C. Control
D. Cache miss
Correct Answer: B

Q74. Branch prediction reduces?
A. Data stalls
B. Control stalls
C. Structural
D. TLB miss
Correct Answer: B

Q75. Delayed branch uses?
A. NOP/branch slot
B. Flush always
C. Predictor
D. Cache
Correct Answer: A

Q76. Pipeline flush penalty equals?
A. Stages remaining
B. Depth of pipe
C. 1 always
D. 0
Correct Answer: B

Q77. 4-stage pipe, 100 instr, no stalls, cycles?
A. 100
B. 103
C. 400
D. 104
Correct Answer: B

Q78. Throughput with cycle 2ns, ideal CPI 1?
A. 500 MIPS
B. 2 MIPS
C. 1000 MIPS
D. 250 MIPS
Correct Answer: A

Q79. Speedup with branch penalty 3, 20% branches?
A. Depends CPI
B. 1.6 degraded
C. 3
D. Ideal
Correct Answer: B

Q80. Superscalar means?
A. Multiple issue per cycle
B. Deeper pipe
C. Vector
D. Multithread
Correct Answer: A

Q81. Superpipelined means?
A. Many narrow stages
B. Multiple pipes
C. VLIW
D. SIMD
Correct Answer: A

Q82. VLIW relies on?
A. Hardware scheduling
B. Compiler scheduling
C. Branch predictor
D. Cache
Correct Answer: B

Q83. Out-of-order needs?
A. Scoreboard/Tomasulo
B. In-order only
C. No rename
D. No buffer
Correct Answer: B

Q84. Register renaming removes?
A. True dep
B. Name dep (WAR/WAW)
C. Control
D. Structural
Correct Answer: A

Q85. Tomasulo uses?
A. Reservation stations
B. Branch stack
C. Victim cache
D. Write buffer
Correct Answer: B

Q86. Speculative execution needs?
A. Reorder buffer
B. Larger cache
C. Slower clock
D. No predictor
Correct Answer: A

Q87. Precise interrupt requires?
A. In-order commit
B. Out-of-order commit
C. No pipeline
D. Flush cache
Correct Answer: A

Q88. MIPS load-use hazard needs?
A. 0 stalls
B. 1 stall/bubble
C. 2 stalls
D. Flush
Correct Answer: A

Q89. Compiler avoids load-use by?
A. Instruction scheduling
B. Loop unroll only
C. Inlining
D. Dead code
Correct Answer: B

Q90. Loop unrolling helps?
A. Reduce branch/data hazards
B. Increase code
C. Both
D. Neither
Correct Answer: A

Q91. CPI pipelined = base +?
A. Stall cycles/instr
B. Clock
C. Depth
D. Cache size
Correct Answer: A

Q92. Amdahl's law for pipeline?
A. Limited by sequential part
B. Unlimited
C. Linear always
D. Exponential
Correct Answer: A

Q93. RISC pipeline friendly because?
A. Fixed length, load-store
B. Complex modes
C. Microcode
D. Variable length
Correct Answer: A

Q94. CISC pipelining difficult due to?
A. Simple ops
B. Variable length/complex
C. Load-store
D. Many regs
Correct Answer: B

Q95. Control memory in Wilkes design holds?
A. Microinstructions
B. Macro ops
C. Data
D. Addresses only
Correct Answer: B

Q96. Horizontal microcode is?
A. Compact
B. Wide, parallel control
C. Vertical
D. Nanocode
Correct Answer: A

Q97. Datapath cycle time set by?
A. Fastest stage
B. Slowest stage
C. Average
D. First stage
Correct Answer: B

Q98. Pipeline register between stages holds?
A. Control only
B. Data+control
C. Clock
D. PC only
Correct Answer: B

Q99. Hazard detection unit in ID stage detects?
A. Load-use
B. Structural
C. WAW
D. Branch taken
Correct Answer: A

Q100. Forwarding paths needed EX-MEM and?
A. MEM-WB
B. ID-IF
C. WB-IF
D. IF-ID
Correct Answer: A

Q101. Memory hierarchy goal?
A. Speed of SRAM cost of disk
B. Speed of cache at cost of SRAM?
C. Average near fastest, cost near cheapest
D. Largest size only
Correct Answer: C

Q102. Locality exploited by hierarchy?
A. Temporal+spatial
B. Only temporal
C. Only spatial
D. None
Correct Answer: A

Q103. SRAM vs DRAM: SRAM is?
A. Dense cheap
B. Fast, no refresh
C. Slow refresh
D. Nonvolatile
Correct Answer: B

Q104. DRAM needs?
A. Refresh
B. No refresh
C. Battery
D. Larger transistors only
Correct Answer: B

Q105. Cache between?
A. CPU-registers
B. CPU-main memory
C. Main-disk
D. I/O-CPU
Correct Answer: A

Q106. Cache hit means?
A. Found in cache
B. Miss
C. Page fault
D. TLB miss
Correct Answer: B

Q107. Hit ratio 0.95, Tc=10ns, Tm=100ns, AMAT?
A. 14.5ns
B. 100ns
C. 10ns
D. 19ns
Correct Answer: A

Q108. AMAT formula?
A. Hit+Miss*Penalty
B. Hit*Miss
C. Miss/Hit
D. Penalty-Hit
Correct Answer: A

Q109. Direct-mapped cache index uses?
A. Tag only
B. Middle bits
C. High bits
D. Offset only
Correct Answer: B

Q110. Fully associative search uses?
A. Index
B. Parallel comparators
C. Decoder
D. Hash only
Correct Answer: B

Q111. Set-associative balances?
A. Cost/miss rate
B. Size only
C. Power only
D. Speed only
Correct Answer: A

Q112. Block size large exploits?
A. Temporal
B. Spatial
C. Both
D. Neither
Correct Answer: B

Q113. Larger block may increase?
A. Miss penalty
B. Hit time always down
C. Tag size up
D. Associativity
Correct Answer: B

Q114. Write-through policy writes to?
A. Cache only
B. Cache+memory
C. Memory only
D. Buffer only
Correct Answer: A

Q115. Write-back uses bit?
A. Valid
B. Dirty
C. Tag
D. LRU
Correct Answer: B

Q116. Write allocate on miss brings block for?
A. Write-through no-allocate
B. Write-back typically
C. Never
D. ROM
Correct Answer: B

Q117. No-write-allocate is common with?
A. Write-back
B. Write-through
C. LRU
D. FIFO
Correct Answer: B

Q118. Valid bit indicates?
A. Dirty
B. Block has valid data
C. LRU
D. Shared
Correct Answer: B

Q119. Tag bits = Addr - (index+offset) example 32b, 1K sets, 32B block?
A. 17
B. 15
C. 20
D. 22
Correct Answer: A

Q120. Cache size = sets*assoc*block. 512 sets,4-way,64B?
A. 64KB
B. 128KB
C. 256KB
D. 32KB
Correct Answer: B

Q121. LRU replacement needs bits for 4-way?
A. 1
B. 2
C. 4
D. 8
Correct Answer: B

Q122. FIFO vs LRU: Belady anomaly in?
A. LRU
B. FIFO
C. Both
D. Neither
Correct Answer: B

Q123. Cold miss is?
A. Compulsory
B. Capacity
C. Conflict
D. Coherence
Correct Answer: B

Q124. Conflict miss reduced by?
A. Larger block
B. Higher associativity
C. Smaller cache
D. Write-through
Correct Answer: B

Q125. Capacity miss reduced by?
A. Larger cache
B. Associativity only
C. Victim always
D. Prefetch only
Correct Answer: A

Q126. Thrashing due to?
A. Conflict/capacity
B. Compulsory
C. Hit
D. Write buffer
Correct Answer: A

Q127. Victim cache holds?
A. Recently evicted
B. Prefetched
C. Write buffer
D. TLB
Correct Answer: A

Q128. Prefetching exploits?
A. Spatial/stride
B. Random
C. LRU
D. Write
Correct Answer: B

Q129. Split I/D cache avoids?
A. Capacity
B. Structural hazard
C. Conflict
D. Coherence
Correct Answer: B

Q130. Unified cache advantage?
A. No interference
B. Flexible allocation
C. Faster hit
D. Less tag
Correct Answer: B

Q131. Main memory typically?
A. SRAM
B. DRAM
C. Flash
D. Magnetic
Correct Answer: B

Q132. ROM is?
A. Volatile
B. Nonvolatile
C. Cache
D. Register
Correct Answer: B

Q133. Virtual memory maps?
A. Physical-virtual
B. Virtual-physical
C. Cache-memory
D. Disk-cache
Correct Answer: B

Q134. Page size typical?
A. 32B
B. 4KB
C. 4MB cache
D. 1B
Correct Answer: B

Q135. Page fault handled by?
A. Hardware only
B. OS
C. Compiler
D. Cache controller
Correct Answer: B

Q136. TLB caches?
A. Data
B. Page table entries
C. Instructions
D. Disk blocks
Correct Answer: B

Q137. TLB miss slower than?
A. Page fault
B. Cache miss? Actually TLB miss < page fault
C. Hit
D. Equal
Correct Answer: B

Q138. Two-level page table saves?
A. Time
B. Space
C. TLB
D. Cache
Correct Answer: B

Q139. Inverted page table size depends on?
A. Virtual
B. Physical frames
C. Page size
D. Process
Correct Answer: B

Q140. Thrashing in VM due to?
A. High locality
B. Over-allocation, low frames
C. Large RAM
D. Fast disk
Correct Answer: B

Q141. Working set model ensures?
A. Locality retained
B. FIFO
C. Belady
D. Segmentation
Correct Answer: A

Q142. Secondary memory example?
A. Registers
B. HDD/SSD
C. SRAM
D. DRAM
Correct Answer: B

Q143. SSD vs HDD: SSD has?
A. Seek time
B. No mechanical seek
C. Slower
D. Magnetic
Correct Answer: B

Q144. Disk access time =?
A. Seek+rotational+transfer
B. Hit+miss
C. CAS only
D. Cycle only
Correct Answer: B

Q145. Average rotational latency 7200 RPM?
A. 8.33ms
B. 4.17ms
C. 2ms
D. 16ms
Correct Answer: B

Q146. RAID 0 provides?
A. Redundancy
B. Striping, no redundancy
C. Mirror
D. Parity
Correct Answer: A

Q147. RAID 1 provides?
A. Striping
B. Mirroring
C. Parity
D. Speed only
Correct Answer: B

Q148. RAID 5 tolerates how many disk failures?
A. 0
B. 1
C. 2
D. All
Correct Answer: B

Q149. Optical vs magnetic: optical is?
A. Faster
B. Removable, slower
C. Volatile
D. SRAM
Correct Answer: B

Q150. Memory interleaving improves?
A. Latency
B. Bandwidth
C. Capacity
D. Reliability
Correct Answer: B

Q151. Low-order interleave uses?
A. High bits
B. Low bits for module
C. Tag
D. Row only
Correct Answer: B

Q152. Burst mode in DRAM (FPM/EDO/SDRAM) exploits?
A. Locality sequential
B. Random
C. Refresh
D. ECC
Correct Answer: A

Q153. ECC can?
A. Detect only
B. Correct single-bit
C. No detection
D. Replace disk
Correct Answer: B

Q154. Parity detects?
A. Even errors
B. Odd/single-bit
C. All
D. Burst
Correct Answer: B

Q155. Cache coherence problem in?
A. Uniprocessor
B. Multiprocessor
C. Unpipelined
D. VM
Correct Answer: B

Q156. MSI/MESI are?
A. Coherence protocols
B. Replacement
C. Bus arb
D. Page replacement
Correct Answer: A

Q157. Write-invalidate vs update: invalidate?
A. Broadcast data
B. Invalidate others
C. Update all
D. No bus
Correct Answer: B

Q158. Snooping uses?
A. Shared bus monitoring
B. Directory
C. OS
D. Compiler
Correct Answer: B

Q159. NUMA vs UMA: NUMA has?
A. Uniform latency
B. Non-uniform
C. No shared
D. Single bus
Correct Answer: B

Q160. Memory-mapped I/O maps devices to?
A. I/O ports
B. Memory addresses
C. Cache
D. Registers only
Correct Answer: B

Q161. Isolated I/O uses?
A. Same addresses
B. Separate instructions/ports
C. Memory
D. DMA only
Correct Answer: B

Q162. Polling vs interrupt: polling?
A. CPU waits/busy
B. Async
C. Efficient
D. DMA
Correct Answer: B

Q163. Interrupt allows?
A. Busy wait
B. Overlap, async service
C. No context switch
D. Sync only
Correct Answer: B

Q164. ISR address via?
A. Polling
B. Vector table
C. Stack
D. Cache
Correct Answer: B

Q165. Interrupt priority handled by?
A. Daisy chain/controller
B. ALU
C. Cache
D. Bus data
Correct Answer: A

Q166. INTR vs NMI: NMI is?
A. Maskable
B. Non-maskable
C. Software
D. Poll
Correct Answer: B

Q167. DMA transfers between?
A. CPU-register
B. Memory-peripheral w/o CPU
C. Cache-CPU
D. ALU-IO
Correct Answer: B

Q168. DMA modes: burst vs cycle-steal?
A. Burst blocks bus
B. Steal interleaves
C. Both
D. Neither
Correct Answer: B

Q169. DMA controller needs?
A. Address+count+control
B. ALU
C. Cache
D. TLB
Correct Answer: A

Q170. Cycle stealing means?
A. CPU halted fully
B. One cycle borrowed
C. Burst
D. Interrupt only
Correct Answer: B

Q171. I/O processor (channel) is?
A. Simple DMA
B. Dedicated I/O CPU
C. ALU
D. Bus
Correct Answer: B

Q172. Synchronous vs async bus: async uses?
A. Clock
B. Handshake
C. Fixed timing
D. Burst only
Correct Answer: B

Q173. Bus arbitration decides?
A. Priority
B. Master
C. Slave speed
D. Address
Correct Answer: B

Q174. Daisy chaining priority depends on?
A. Position
B. Request time
C. Device speed
D. Random
Correct Answer: A

Q175. Programmed I/O uses?
A. Interrupts
B. CPU instructions
C. DMA
D. Channel
Correct Answer: B

Q176. Interrupt-driven I/O saves CPU vs?
A. DMA
B. Programmed
C. Channel
D. Cache
Correct Answer: B

Q177. Which fastest for bulk transfer?
A. Programmed
B. Interrupt
C. DMA
D. Polling
Correct Answer: C

Q178. Device status checked via?
A. Data reg
B. Status reg
C. Address
D. Cache
Correct Answer: B

Q179. UART is for?
A. Parallel
B. Serial
C. DMA
D. Disk
Correct Answer: B

Q180. SCSI/USB are?
A. CPU buses
B. I/O buses/interfaces
C. Memory
D. ALU
Correct Answer: B

Q181. Throughput of bus = width*freq example 32b 100MHz?
A. 400MB/s
B. 100MB/s
C. 3200MB/s
D. 32MB/s
Correct Answer: A

Q182. Bus width 64b, 66MHz throughput?
A. 528MB/s
B. 66MB/s
C. 4224MB/s
D. 132MB/s
Correct Answer: A

Q183. Daisy chain fails if device?
A. Fast
B. Fails/powered off breaks chain
C. Slow
D. Multiple
Correct Answer: B

Q184. Polling overhead is?
A. Low
B. High CPU waste
C. Zero
D. DMA-like
Correct Answer: B

Q185. Interrupt latency is?
A. Request to service start
B. Service time
C. Transfer
D. Return
Correct Answer: A

Q186. Multiple interrupts handled by?
A. Priority + masking
B. Single vector
C. Poll only
D. Cache
Correct Answer: A

Q187. Software interrupt is?
A. Trap/syscall
B. Hardware
C. NMI
D. DMA
Correct Answer: A

Q188. Edge vs level triggered: level needs?
A. Ack to clear
B. Pulse only
C. No ack
D. Poll
Correct Answer: A

Q189. IOP offloads?
A. ALU
B. CPU I/O burden
C. Memory
D. Cache
Correct Answer: B

Q190. Spooling overlaps?
A. CPU-I/O via buffer
B. ALU ops
C. Cache
D. Pipeline
Correct Answer: B

Q191. Buffer vs cache in I/O: buffer?
A. Speed mismatch absorb
B. Locality
C. Coherence
D. Replacement
Correct Answer: A

Q192. Double buffering allows?
A. Overlap I/O-compute
B. Half speed
C. No overlap
D. Cache coherence
Correct Answer: A

Q193. Memory-mapped I/O advantage?
A. Separate instructions
B. Use load/store, flexible
C. Port saving
D. Faster DMA
Correct Answer: B

Q194. Isolated I/O advantage?
A. Large space
B. No memory space waste, protection
C. Load/store
D. Cacheable
Correct Answer: B

Q195. Bus mastership by DMA needs?
A. HOLD/HLDA
B. INT
C. NMI
D. READY
Correct Answer: B

Q196. Flyby DMA transfers?
A. Via controller
B. Direct mem-device
C. Via CPU
D. Via cache
Correct Answer: B

Q197. I/O mapped to cacheable memory causes?
A. Stale data
B. Faster always safe
C. No issue
D. Coherence ok
Correct Answer: A

Q198. Uncacheable I/O region avoids?
A. Speed
B. Stale/coherence issues
C. Latency
D. Interrupts
Correct Answer: B

Q199. Throughput vs latency in I/O: streaming needs?
A. Low latency
B. High throughput
C. Both low
D. Neither
Correct Answer: B

Q200. Best bulk disk backup interface choice?
A. Programmed PIO
B. DMA/channel + buffering
C. Polling
D. Single-byte interrupt
Correct Answer: B

---
## ANSWER KEY
1-C 2-B 3-C 4-B 5-B 6-B 7-B 8-A 9-C 10-C
11-A 12-B 13-A 14-B 15-A 16-B 17-A 18-B 19-A 20-B
21-B 22-B 23-A 24-C 25-B 26-B 27-B 28-A 29-C 30-C
31-B 32-B 33-A 34-A 35-B 36-A 37-B 38-B 39-A 40-B
41-A 42-A 43-A 44-A 45-A 46-A 47-B 48-C 49-A 50-B
51-A 52-B 53-B 54-A 55-A 56-A 57-A 58-A 59-B 60-B
61-A 62-B 63-A 64-B 65-B 66-A 67-B 68-B 69-A 70-B
71-A 72-A 73-B 74-B 75-A 76-B 77-B 78-A 79-B 80-A
81-A 82-B 83-B 84-A 85-B 86-A 87-A 88-A 89-B 90-A
91-A 92-A 93-A 94-B 95-B 96-A 97-B 98-B 99-A 100-A
101-C 102-A 103-B 104-B 105-A 106-B 107-A 108-A 109-B 110-B
111-A 112-B 113-B 114-A 115-B 116-B 117-B 118-B 119-A 120-B
121-B 122-B 123-B 124-B 125-A 126-A 127-A 128-B 129-B 130-B
131-B 132-B 133-B 134-B 135-B 136-B 137-B 138-B 139-B 140-B
141-A 142-B 143-B 144-B 145-B 146-A 147-B 148-B 149-B 150-B
151-B 152-A 153-B 154-B 155-B 156-A 157-B 158-B 159-B 160-B
161-B 162-B 163-B 164-B 165-A 166-B 167-B 168-B 169-A 170-B
171-B 172-B 173-B 174-A 175-B 176-B 177-C 178-B 179-B 180-B
181-A 182-A 183-B 184-B 185-A 186-A 187-A 188-A 189-B 190-B
191-A 192-A 193-B 194-B 195-B 196-B 197-A 198-B 199-B 200-B
