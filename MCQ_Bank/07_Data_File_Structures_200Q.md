# Topic 7: Data and File Structures

**Syllabus:** Data structures: Data, Information, Definition of data structure, Arrays, stacks, queues, linked lists, trees, graphs, priority queues, and heaps; File Structures: Fields, records and files, Sequential, direct, index-sequential and relative files, Hashing, inverted lists and multi-lists, B trees and B+ trees.

Q1. Array random access time?
A. O(1)
B. O(n)
C. O(log n)
D. O(n^2)
Correct Answer: A

Q2. Array insertion at front cost?
A. O(1)
B. O(n)
C. O(log n)
D. O(0)
Correct Answer: B

Q3. Row-major address: base 1000, int 4B, a[3][4], a[1][2]?
A. 1024
B. 1020
C. 1044
D. 1008
Correct Answer: A

Q4. Sparse matrix best stored as?
A. 2D array
B. Triplet/linked
C. Stack
D. Queue
Correct Answer: B

Q5. Stack discipline?
A. FIFO
B. LIFO
C. Priority
D. Random
Correct Answer: B

Q6. Stack operations?
A. Enqueue/dequeue
B. Push/pop
C. Insert/delete arbitrary
D. Sort
Correct Answer: B

Q7. Infix a+b*c precedence gives?
A. (a+b)*c
B. a+(b*c)
C. a*b+c
D. abc+*
Correct Answer: B

Q8. Postfix ab+c* evaluates a=2,b=3,c=4?
A. 20
B. 14
C. 10
D. 24
Correct Answer: A

Q9. Prefix +*234 equals?
A. 14
B. 20
C. 10
D. 24
Correct Answer: A

Q10. Stack for recursion stores?
A. Heap
B. Activation records
C. Globals
D. Code
Correct Answer: B

Q11. Balanced parentheses uses?
A. Queue
B. Stack
C. Tree
D. Graph
Correct Answer: B

Q12. Infix to postfix needs stack for?
A. Operands
B. Operators
C. Output
D. Numbers
Correct Answer: B

Q13. Postfix evaluation complexity?
A. O(n^2)
B. O(n)
C. O(log n)
D. O(2^n)
Correct Answer: B

Q14. Two stacks in one array: overflow when?
A. One full
B. Total size met
C. Both empty
D. Never
Correct Answer: B

Q15. Queue discipline?
A. LIFO
B. FIFO
C. FILO
D. Random
Correct Answer: B

Q16. Circular queue full condition (size N)?
A. front==rear
B. (rear+1)%N==front
C. rear==0
D. front==0
Correct Answer: B

Q17. Queue via two stacks: enqueue O?
A. O(n)
B. O(1) amortized
C. O(log n)
D. O(n^2)
Correct Answer: B

Q18. Deque allows?
A. One end
B. Both ends
C. Priority
D. Sorted
Correct Answer: B

Q19. Priority queue best impl?
A. Array
B. Heap
C. Stack
D. Linked unsorted
Correct Answer: B

Q20. BFS uses?
A. Stack
B. Queue
C. Heap
D. Tree
Correct Answer: B

Q21. DFS uses?
A. Queue
B. Stack/recursion
C. Heap
D. Array
Correct Answer: B

Q22. Singly linked list search O?
A. O(1)
B. O(n)
C. O(log n)
D. O(0)
Correct Answer: B

Q23. Insert at head DLL/SLL O?
A. O(n)
B. O(1)
C. O(log n)
D. O(n^2)
Correct Answer: B

Q24. Delete given node pointer (no head) SLL?
A. O(n)
B. O(1) copy next
C. O(log n)
D. Impossible
Correct Answer: B

Q25. Doubly linked allows?
A. Forward only
B. Both directions
C. Random
D. Indexed
Correct Answer: B

Q26. Circular list last->next points to?
A. Null
B. First
C. Itself only
D. Middle
Correct Answer: B

Q27. Linked list vs array: linked?
A. Random access
B. Dynamic, no shift
C. Cache friendly
D. Less memory
Correct Answer: B

Q28. Reverse SLL complexity?
A. O(n^2)
B. O(n) time O(1) space
C. O(log n)
D. O(n log n)
Correct Answer: B

Q29. Detect cycle uses?
A. Two stacks
B. Floyd slow/fast
C. BFS
D. Sorting
Correct Answer: B

Q30. Middle of list in one pass?
A. Two pointers
B. Count only
C. Reverse
D. Sort
Correct Answer: A

Q31. Stack via linked list push O?
A. O(n)
B. O(1)
C. O(log n)
D. O(n^2)
Correct Answer: B

Q32. Polynomial add via sorted LL O?
A. O(1)
B. O(n+m)
C. O(n*m)
D. O(log n)
Correct Answer: B

Q33. Tree height with n nodes min?
A. n
B. log n
C. n log n
D. 1
Correct Answer: B

Q34. Full binary tree n nodes: leaves?
A. n/2
B. (n+1)/2
C. n-1
D. log n
Correct Answer: B

Q35. Max nodes at level l (root 0)?
A. l
B. 2^l
C. 2l
D. l^2
Correct Answer: B

Q36. Max nodes height h (root 1)?
A. 2^h
B. 2^h-1
C. h^2
D. 2h
Correct Answer: B

Q37. Inorder of BST gives?
A. Unsorted
B. Sorted
C. Reverse
D. Level
Correct Answer: B

Q38. Preorder sequence root?
A. Last
B. First
C. Middle
D. Random
Correct Answer: C

Q39. Postorder root?
A. First
B. Last
C. Middle
D. None
Correct Answer: B

Q40. Inorder: left-root-right; preorder of 4,2,1,3,6,5,7?
A. 1,2,3,4,5,6,7
B. 4,2,1,3,6,5,7
C. 1,3,2,5,7,6,4
D. 4,2,6,1,3,5,7
Correct Answer: B

Q41. BST search worst O?
A. O(log n)
B. O(n) skewed
C. O(1)
D. O(n log n)
Correct Answer: B

Q42. BST insert 10,5,15,3,7: height?
A. 1
B. 2
C. 3
D. 4
Correct Answer: C

Q43. BST delete node with two children replace with?
A. Any
B. Inorder succ/pred
C. Root
D. Leaf
Correct Answer: B

Q44. AVL balance factor?
A. 0 only
B. -1,0,1
C. -2 to 2
D. Any
Correct Answer: B

Q45. AVL rotations for LL?
A. Left
B. Right
C. LR
D. RL
Correct Answer: B

Q46. AVL search O?
A. O(n)
B. O(log n)
C. O(1)
D. O(n^2)
Correct Answer: B

Q47. Insert sorted into AVL n items O?
A. O(n)
B. O(n log n)
C. O(n^2)
D. O(log n)
Correct Answer: B

Q48. Splay/Red-black height?
A. O(n)
B. O(log n) amortized/guaranteed
C. O(1)
D. O(n^2)
Correct Answer: B

Q49. B-tree order m: max children?
A. m-1
B. m
C. m+1
D. 2m
Correct Answer: B

Q50. B+ tree stores data?
A. All nodes
B. Leaves only (+ linked)
C. Root only
D. Internal
Correct Answer: B

Q51. B/B+ good for?
A. RAM
B. Disk/file systems
C. Cache only
D. Stack
Correct Answer: B

Q52. B-tree search O?
A. O(1)
B. O(log_t n)
C. O(n)
D. O(n log n)
Correct Answer: B

Q53. Heap property max-heap?
A. Parent<=child
B. Parent>=child
C. Sorted
D. Balanced BST
Correct Answer: B

Q54. Build heap O?
A. O(n log n)
B. O(n)
C. O(log n)
D. O(1)
Correct Answer: B

Q55. Insert heap O?
A. O(1)
B. O(log n)
C. O(n)
D. O(n log n)
Correct Answer: B

Q56. Extract-max O?
A. O(1)
B. O(log n)
C. O(n)
D. O(0)
Correct Answer: B

Q57. Heapsort complexity?
A. O(n)
B. O(n log n) worst
C. O(n^2)
D. O(log n)
Correct Answer: B

Q58. Heapsort space?
A. O(n)
B. O(1) auxiliary
C. O(log n)
D. O(n^2)
Correct Answer: B

Q59. Priority queue extract-min heap?
A. O(1)
B. O(log n)
C. O(n)
D. O(n log n)
Correct Answer: B

Q60. Array heap parent of i (0-index)?
A. i/2
B. (i-1)/2
C. 2i
D. 2i+1
Correct Answer: B

Q61. Graph representations: adjacency matrix space?
A. O(V)
B. O(V^2)
C. O(E)
D. O(1)
Correct Answer: B

Q62. Adjacency list space?
A. O(V^2)
B. O(V+E)
C. O(E^2)
D. O(1)
Correct Answer: B

Q63. BFS complexity?
A. O(V)
B. O(V+E)
C. O(E^2)
D. O(V^2) always
Correct Answer: B

Q64. DFS complexity?
A. O(V+E)
B. O(V^2)
C. O(E log V)
D. O(V log V)
Correct Answer: A

Q65. BFS shortest path (unweighted) from source?
A. No
B. Yes
C. Only DFS
D. Only Dijkstra
Correct Answer: B

Q66. DFS for cycle in directed uses?
A. Visited only
B. Colors/recursion stack
C. Queue
D. Heap
Correct Answer: B

Q67. Topological sort uses?
A. BFS Kahn / DFS finish
B. Dijkstra
C. MST
D. Heap
Correct Answer: A

Q68. Topological possible only for?
A. Cyclic
B. DAG
C. Undirected
D. Complete
Correct Answer: A

Q69. Dijkstra handles?
A. Negative weights
B. Non-negative
C. All
D. Unweighted only
Correct Answer: B

Q70. Dijkstra with binary heap O?
A. O(V^2)
B. O((V+E) log V)
C. O(V+E)
D. O(E log E) only
Correct Answer: B

Q71. Bellman-Ford handles negatives? Complexity?
A. No, O(V+E)
B. Yes (no neg cycle), O(VE)
C. Yes all, O(log)
D. No
Correct Answer: B

Q72. Floyd-Warshall O?
A. O(V+E)
B. O(V^3)
C. O(V^2)
D. O(E log V)
Correct Answer: B

Q73. MST Kruskal uses?
A. Heap only
B. Sort + Union-Find
C. BFS
D. DFS
Correct Answer: B

Q74. Prim with heap O?
A. O(V^2)
B. O(E log V)
C. O(VE)
D. O(V^3)
Correct Answer: B

Q75. Union-Find with path compression ~?
A. O(n)
B. O(alpha(n))
C. O(log n) always
D. O(n^2)
Correct Answer: B

Q76. Pseudocode: for i=1..n for j=1..i print: complexity?
A. O(n)
B. O(n^2)
C. O(log n)
D. O(n log n)
Correct Answer: A

Q77. Pseudocode: while n>1 n=n/2: complexity?
A. O(n)
B. O(log n)
C. O(n log n)
D. O(1)
Correct Answer: B

Q78. T(n)=2T(n/2)+n gives?
A. O(n)
B. O(n log n)
C. O(n^2)
D. O(log n)
Correct Answer: B

Q79. T(n)=T(n-1)+n gives?
A. O(n)
B. O(n^2)
C. O(log n)
D. O(2^n)
Correct Answer: B

Q80. Binary search O?
A. O(n)
B. O(log n)
C. O(1)
D. O(n log n)
Correct Answer: B

Q81. Linear search worst?
A. O(log n)
B. O(n)
C. O(1)
D. O(n^2)
Correct Answer: B

Q82. Quick sort avg/worst?
A. O(n)/O(n^2)
B. O(n log n) avg, O(n^2) worst
C. O(n^2)/O(n)
D. O(log n)
Correct Answer: B

Q83. Merge sort?
A. O(n^2)
B. O(n log n) all
C. O(n)
D. O(log n)
Correct Answer: B

Q84. Output: stack push 1,2,3 pop, push 4 pop,pop: order?
A. 3,4,2
B. 3,2,1
C. 1,2,3
D. 4,3,2
Correct Answer: A

Q85. Queue enqueue 1,2,3 dequeue, enqueue 4 dequeue,dequeue: order?
A. 1,2,3
B. 2,3
C. 1,2
D. 1,4,2
Correct Answer: A

Q86. Postfix 5 1 2 + 4 * + 3 - =?
A. 14
B. 12
C. 11
D. 10
Correct Answer: A

Q87. Prefix - + 2 3 * 4 5 =? ( (2+3)-(4*5) )
A. -15
B. 15
C. 25
D. 5
Correct Answer: A

Q88. Infix (a+b)*(c-d) postfix?
A. ab+cd-*
B. ab+cd*-
C. abc+d-*
D. ab*cd+-
Correct Answer: A

Q89. Ackermann/recurrence depth uses?
A. Heap
B. Stack
C. Queue
D. Graph
Correct Answer: B

Q90. Tail recursion优化 to?
A. Loop
B. More stack
C. Heap
D. Tree
Correct Answer: A

Q91. BST inorder 1,2,3,4,5; preorder 3,1,2,4,5 root?
A. 1
B. 3
C. 5
D. 2
Correct Answer: B

Q92. AVL after insert balance 2 at root left-heavy, left child balanced: rotation?
A. L
B. R
C. LR
D. RL
Correct Answer: B

Q93. Min heap [10,20,30,40] insert 5: new root?
A. 10
B. 5
C. 20
D. 30
Correct Answer: B

Q94. Max heap extract root [20,15,10]: next root?
A. 20
B. 15
C. 10
D. 5
Correct Answer: B

Q95. Height of heap n nodes?
A. O(n)
B. O(log n)
C. O(1)
D. O(n log n)
Correct Answer: B

Q96. Level-order traversal uses?
A. Stack
B. Queue
C. Recursion
D. Heap
Correct Answer: B

Q97. Inorder without recursion uses?
A. Explicit stack
B. Queue
C. Heap
D. Array
Correct Answer: B

Q98. Expression tree leaves are?
A. Operators
B. Operands
C. Root
D. Null
Correct Answer: B

Q99. Huffman tree is for?
A. Sorting
B. Compression
C. Searching
D. MST
Correct Answer: B

Q100. Huffman greedy uses?
A. Stack
B. Min-heap
C. Queue
D. BST
Correct Answer: B

Q101. File: sequential access best for?
A. Random
B. Tape/batch
C. Indexed
D. Direct
Correct Answer: B

Q102. Direct/hash file gives?
A. Sequential
B. Random O(1) avg
C. Sorted
D. Slow
Correct Answer: B

Q103. Indexed sequential (ISAM) combines?
A. Sequential+index
B. Hash only
C. Random only
D. Linked
Correct Answer: A

Q104. Relative file record address via?
A. Key->offset calc
B. Index
C. Scan
D. Hash chain
Correct Answer: A

Q105. Master vs transaction file: master?
A. Temporary
B. Permanent base
C. Log
D. Index
Correct Answer: B

Q106. Sorting large file uses?
A. Quick in RAM
B. External k-way merge
C. Bubble
D. Heap only
Correct Answer: B

Q107. Blocking factor =?
A. File/block
B. Block/record
C. Records per block
D. Blocks per file
Correct Answer: C

Q108. Unblocked vs blocked: blocked?
A. Wasteful
B. Reduces I/O
C. Slower
D. Fragmented
Correct Answer: B

Q109. Overflow in ISAM handled by?
A. Rehash
B. Overflow area/chain
C. Split always
D. Ignore
Correct Answer: B

Q110. B+ tree vs ISAM: B+?
A. Static
B. Dynamic balanced
C. Sequential only
D. Hash
Correct Answer: B

Q111. Hashing: h(k) maps to?
A. Record
B. Bucket/address
C. File
D. Index
Correct Answer: B

Q112. Collision occurs when?
A. Different keys same address
B. Same key
C. Full file
D. Empty
Correct Answer: A

Q113. Chaining resolves by?
A. Rehash
B. Linked list per bucket
C. Probing
D. Double file
Correct Answer: B

Q114. Open addressing stores?
A. Elsewhere linked
B. In table itself
C. Overflow file
D. Index
Correct Answer: B

Q115. Linear probing suffers?
A. No clustering
B. Primary clustering
C. Secondary
D. No probe
Correct Answer: B

Q116. Double hashing uses?
A. One function
B. Two functions
C. Chaining
D. Sorting
Correct Answer: B

Q117. Load factor =?
A. n/m
B. m/n
C. collisions
D. buckets/records
Correct Answer: A

Q118. Rehash when load?
A. Low
B. High (>0.7-0.8)
C. Zero
D. Never
Correct Answer: B

Q119. Perfect hashing for?
A. Dynamic
B. Static set, no collisions
C. All
D. Overflow
Correct Answer: B

Q120. Extendible hashing uses?
A. Fixed array
B. Directory + global depth
C. Chain only
D. B-tree
Correct Answer: B

Q121. Inverted list is?
A. Forward index
B. Key -> list of records
C. Sequential
D. Heap
Correct Answer: B

Q122. Inverted file good for?
A. Range primary
B. Secondary key queries
C. Sequential batch
D. Sorting
Correct Answer: B

Q123. Multi-list links records with?
A. Arrays
B. Linked pointers per attribute
C. Hash
D. Tree
Correct Answer: B

Q124. Multi-list vs inverted: multi-list?
A. Separate index
B. Embedded links, slower traverse
C. Faster
D. No links
Correct Answer: B

Q125. Cellular multilist partitions into?
A. Buckets
B. Cells/subfiles
C. Blocks
D. Trees
Correct Answer: B

Q126. Index dense vs sparse: dense?
A. One per block
B. One per record
C. One per file
D. None
Correct Answer: B

Q127. Primary index on?
A. Non-key
B. Ordered key
C. Unordered
D. Secondary
Correct Answer: B

Q128. Secondary index needs?
A. Nothing
B. Extra level/bucket pointers
C. Sorted file
D. Hash only
Correct Answer: B

Q129. Clustering index file?
A. Unordered
B. Ordered on non-key
C. Hash
D. Direct
Correct Answer: B

Q130. B-tree node split when?
A. Underflow
B. Overflow/full
C. Empty
D. Delete only
Correct Answer: B

Q131. B-tree min keys (order m)?
A. m
B. ceil(m/2)-1
C. m-1
D. m/2+1
Correct Answer: B

Q132. B+ internal vs leaf: internal?
A. Data
B. Keys+pointers only
C. Records
D. Bitmap
Correct Answer: B

Q133. B+ range scan via?
A. Root only
B. Leaf linked list
C. Hash
D. Stack
Correct Answer: B

Q134. Trie is for?
A. Numbers
B. Strings/prefixes
C. Graphs
D. Heaps
Correct Answer: B

Q135. Trie search O?
A. O(n)
B. O(L) length
C. O(log n)
D. O(1)
Correct Answer: B

Q136. ISAM static vs B+ dynamic: ISAM degrades with?
A. Queries
B. Inserts/overflow
C. Reads
D. Deletes only
Correct Answer: A

Q137. VSAM is?
A. IBM dynamic B-tree-like
B. Hash
C. Sequential only
D. Inverted
Correct Answer: A

Q138. File directory holds?
A. Data
B. Metadata/extents
C. Indexes
D. Records
Correct Answer: B

Q139. Extent is?
A. Record
B. Contiguous blocks
C. File
D. Bit
Correct Answer: B

Q140. Fragmentation internal vs external: external?
A. Wasted inside block
B. Scattered free space
C. No waste
D. Inode
Correct Answer: B

Q141. Linked allocation file suffers?
A. Random access
B. Sequential
C. Sharing
D. Growth
Correct Answer: A

Q142. Indexed allocation (inode) supports?
A. Sequential only
B. Random + dynamic
C. Tape
D. No growth
Correct Answer: B

Q143. FAT vs inode: FAT?
A. Per-file index
B. Central table chain
C. Extents
D. B-tree
Correct Answer: B

Q144. Journaling FS for?
A. Speed only
B. Crash recovery
C. Compression
D. Encryption
Correct Answer: B

Q145. Pseudocode binary search mid=(l+h)/2; overflow safe?
A. Yes always
B. Use l+(h-l)/2
C. No fix
D. Use float
Correct Answer: B

Q146. Output: fun(n){if n<=1 return 1; return n*fun(n-1);} fun(4)?
A. 12
B. 24
C. 16
D. 4
Correct Answer: B

Q147. Output: fib iterative n=6 (0,1...)?
A. 5
B. 8
C. 13
D. 6
Correct Answer: B

Q148. Tower of Hanoi moves n=3?
A. 6
B. 7
C. 8
D. 9
Correct Answer: B

Q149. Complexity Hanoi?
A. O(n)
B. O(2^n)
C. O(n^2)
D. O(n log n)
Correct Answer: B

Q150. Output queue BFS from A: A->B,C; B->D; C->D. Order?
A. A,B,C,D
B. A,C,B,D
C. A,D,B,C
D. A,B,D,C
Correct Answer: A

Q151. DFS from A same graph (B first) order?
A. A,B,D,C
B. A,B,C,D
C. A,C,D,B
D. A,D,C,B
Correct Answer: A

Q152. Dijkstra A->D weights AB1,AC4,BD2,CD1 shortest?
A. 5
B. 3
C. 4
D. 2
Correct Answer: B

Q153. Kruskal picks edges sorted; first?
A. Largest
B. Smallest acyclic
C. Random
D. Last
Correct Answer: B

Q154. Stable sort preserves?
A. Speed
B. Equal order
C. Memory
D. Complexity
Correct Answer: C

Q155. Which stable O(n log n)?
A. Quick
B. Heap
C. Merge
D. Selection
Correct Answer: B

Q156. Counting sort O?
A. O(n log n)
B. O(n+k)
C. O(n^2)
D. O(log n)
Correct Answer: B

Q157. Radix sort base?
A. Comparisons
B. Digit passes
C. Heap
D. Divide
Correct Answer: B

Q158. Bucket sort avg?
A. O(n^2)
B. O(n+k) avg linear uniform
C. O(n log n) always
D. O(log n)
Correct Answer: B

Q159. Lower bound comparison sort?
A. O(n)
B. Omega(n log n)
C. O(log n)
D. O(1)
Correct Answer: B

Q160. Best for nearly sorted?
A. Merge
B. Insertion O(n)
C. Quick
D. Heap
Correct Answer: B

Q161. Best for linked list sort?
A. Quick array
B. Merge (no random)
C. Heap
D. Counting
Correct Answer: B

Q162. Recursion depth quick worst?
A. O(log n)
B. O(n)
C. O(1)
D. O(n log n)
Correct Answer: B

Q163. Tail recursion factorial space without opt?
A. O(1)
B. O(n)
C. O(log n)
D. O(n^2)
Correct Answer: B

Q164. Graph bipartite check via?
A. Dijkstra
B. BFS coloring
C. MST
D. Topo
Correct Answer: B

Q165. Articulation point via?
A. BFS only
B. DFS low/disc
C. Dijkstra
D. Union
Correct Answer: B

Q166. Strongly connected (directed) via?
A. BFS once
B. Kosaraju/Tarjan
C. MST
D. Topo
Correct Answer: B

Q167. Cycle undirected detection via?
A. Union-Find
B. Topo
C. Dijkstra
D. Heap
Correct Answer: B

Q168. AVL delete O?
A. O(1)
B. O(log n)
C. O(n)
D. O(n log n)
Correct Answer: B

Q169. Splay amortized O?
A. O(1)
B. O(log n)
C. O(n)
D. O(n^2)
Correct Answer: B

Q170. 2-3 tree is?
A. Binary
B. Balanced multiway, precursor B-tree
C. Heap
D. Trie
Correct Answer: B

Q171. Red-black vs AVL: RB?
A. Stricter
B. Looser, fewer rotations
C. Unbalanced
D. Array
Correct Answer: B

Q172. Segment tree query O?
A. O(1)
B. O(log n)
C. O(n)
D. O(n log n)
Correct Answer: B

Q173. Fenwick tree for?
A. Prefix sums
B. Sorting
C. MST
D. Strings
Correct Answer: B

Q174. Disjoint set union by rank keeps?
A. Height log
B. List
C. Stack
D. Queue
Correct Answer: B

Q175. Open hashing load >1 possible?
A. No
B. Yes (chaining)
C. Never
D. Only closed
Correct Answer: B

Q176. Closed hashing load must be?
A. >1
B. <=1
C. Any
D. 0
Correct Answer: B

Q177. Expected probe linear load 0.5?
A. 1.5
B. 2.5
C. 1
D. 5
Correct Answer: A

Q178. Double hashing probe sequence depends on?
A. Key
B. Table size only
C. Load only
D. Random
Correct Answer: B

Q179. Cuckoo hashing uses?
A. One table
B. Two functions/displacement
C. Chaining
D. Sorting
Correct Answer: B

Q180. Bloom filter may give?
A. False negative
B. False positive, no false negative
C. Exact
D. No error
Correct Answer: B

Q181. B+ fanout 100, height 3 capacity ~?
A. 1M
B. 1M? 100^3=1M
C. 300
D. 10000
Correct Answer: B

Q182. Height balanced ensures disk accesses?
A. Many
B. Few/logarithmic
C. Linear
D. Random
Correct Answer: B

Q183. Index sequential search steps?
A. Direct only
B. Index + data block
C. Full scan
D. Hash
Correct Answer: B

Q184. Cylinder/track/sector locality: place related on?
A. Random cylinders
B. Same cylinder
C. Different disks
D. Tape
Correct Answer: B

Q185. RAID + B-tree: RAID helps?
A. CPU
B. I/O parallelism
C. Height
D. Keys
Correct Answer: B

Q186. Log file for recovery is?
A. Random
B. Sequential append
C. Hash
D. Indexed
Correct Answer: B

Q187. Checkpoint file truncates?
A. Data
B. Log redo
C. Index
D. Directory
Correct Answer: B

Q188. Two-phase commit for?
A. Single DB
B. Distributed atomic
C. Sorting
D. Indexing
Correct Answer: B

Q189. Shadowing vs logging: shadow?
A. Log
B. Copy-on-write
C. Lock
D. Timestamp
Correct Answer: B

Q190. Pseudocode: sum=0; for i=1..n sum+=i; sum=?
A. n(n+1)/2
B. n^2
C. 2^n
D. n log n
Correct Answer: A

Q191. Output: p=1; for i=1..4 p*=i; p=?
A. 6
B. 24
C. 12
D. 10
Correct Answer: B

Q192. Output: x=0; for i=0..3 for j=0..3 x++; x=?
A. 12
B. 16
C. 9
D. 7
Correct Answer: B

Q193. Recursion T(n)=T(n/2)+1 -> iterative?
A. Linear
B. Binary search-like log
C. Quadratic
D. Exponential
Correct Answer: B

Q194. Master theorem needs?
A. Any recurrence
B. Divide-conquer aT(n/b)+f
C. Linear
D. Tail
Correct Answer: B

Q195. Amortized stack multi-pop analysis O per op?
A. O(n)
B. O(1)
C. O(log n)
D. O(n^2)
Correct Answer: B

Q196. Dynamic array double on full amortized push?
A. O(n^2)
B. O(1)
C. O(log n)
D. O(n)
Correct Answer: B

Q197. Circular buffer queue full vs empty distinguish by?
A. Size/count or sacrifice slot
B. Values
C. Pointers equal always full
D. Flags only data
Correct Answer: A

Q198. Priority queue via sorted array insert/extract?
A. O(1)/O(n)
B. O(n)/O(1) or vice versa
C. O(log n) both
D. O(1) both
Correct Answer: B

Q199. Best structure for LRU cache?
A. Array
B. Hash + DLL
C. Stack
D. BST
Correct Answer: B

Q200. Best for phone prefix autocomplete?
A. Heap
B. Trie
C. Graph
D. Queue
Correct Answer: B

---
## ANSWER KEY
1-A 2-B 3-A 4-B 5-B 6-B 7-B 8-A 9-A 10-B
11-B 12-B 13-B 14-B 15-B 16-B 17-B 18-B 19-B 20-B
21-B 22-B 23-B 24-B 25-B 26-B 27-B 28-B 29-B 30-A
31-B 32-B 33-B 34-B 35-B 36-B 37-B 38-C 39-B 40-B
41-B 42-C 43-B 44-B 45-B 46-B 47-B 48-B 49-B 50-B
51-B 52-B 53-B 54-B 55-B 56-B 57-B 58-B 59-B 60-B
61-B 62-B 63-B 64-A 65-B 66-B 67-A 68-A 69-B 70-B
71-B 72-B 73-B 74-B 75-B 76-A 77-B 78-B 79-B 80-B
81-B 82-B 83-B 84-A 85-A 86-A 87-A 88-A 89-B 90-A
91-B 92-B 93-B 94-B 95-B 96-B 97-B 98-B 99-B 100-B
101-B 102-B 103-A 104-A 105-B 106-B 107-C 108-B 109-B 110-B
111-B 112-A 113-B 114-B 115-B 116-B 117-A 118-B 119-B 120-B
121-B 122-B 123-B 124-B 125-B 126-B 127-B 128-B 129-B 130-B
131-B 132-B 133-B 134-B 135-B 136-A 137-A 138-B 139-B 140-B
141-A 142-B 143-B 144-B 145-B 146-B 147-B 148-B 149-B 150-A
151-A 152-B 153-B 154-C 155-B 156-B 157-B 158-B 159-B 160-B
161-B 162-B 163-B 164-B 165-B 166-B 167-B 168-B 169-B 170-B
171-B 172-B 173-B 174-B 175-B 176-B 177-A 178-B 179-B 180-B
181-B 182-B 183-B 184-B 185-B 186-B 187-B 188-B 189-B 190-A
191-B 192-B 193-B 194-B 195-B 196-B 197-A 198-B 199-B 200-B
