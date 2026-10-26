# Topic 6: Relational Database Design and SQL

**Syllabus:** E-R diagrams: E-R diagrams and their transformation to relational design, Normalization: 1NF, 2NF, 3NF, BCNF and 4NF, Limitations of 4NF and BCNF, SQL: Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL) commands, Database objects like Views, indexes, sequences, synonyms, data dictionary.

Q1. Entity set is?
A. Collection of similar entities
B. Attribute
C. Relation
D. Tuple
Correct Answer: A

Q2. Strong entity has?
A. No key
B. Primary key
C. Partial key
D. Foreign only
Correct Answer: B

Q3. Weak entity depends on?
A. Itself
B. Owner/identifying
C. Attribute
D. Relationship
Correct Answer: B

Q4. Weak entity key is?
A. Primary
B. Partial discriminator + owner key
C. Candidate
D. Surrogate only
Correct Answer: B

Q5. Relationship degree 2 is?
A. Unary
B. Binary
C. Ternary
D. N-ary
Correct Answer: B

Q6. Recursive relationship example?
A. Student-Course
B. Employee supervises Employee
C. Customer-Order
D. Book-Author
Correct Answer: B

Q7. Cardinality 1:N means?
A. One to one
B. One to many
C. Many to many
D. None
Correct Answer: B

Q8. Participation total means?
A. Optional
B. Mandatory
C. Partial
D. Multivalued
Correct Answer: B

Q9. ER to tables: 1:1 total both sides merged into?
A. Two tables
B. Single table
C. Three
D. None
Correct Answer: B

Q10. M:N relationship transforms to?
A. New table with both FKs
B. Add FK one side
C. Merge
D. No table
Correct Answer: A

Q11. 1:N transforms by?
A. New table
B. FK on N side
C. FK on 1 side
D. Merge always
Correct Answer: B

Q12. Multivalued attribute maps to?
A. New table
B. Single column
C. Ignore
D. Primary key
Correct Answer: A

Q13. Composite attribute maps to?
A. Single column
B. Component columns
C. New table
D. FK
Correct Answer: A

Q14. Derived attribute stored?
A. Always
B. Usually not
C. As key
D. As FK
Correct Answer: B

Q15. Primary key constraint ensures?
A. Null allowed
B. Unique+not null
C. Duplicate
D. Foreign
Correct Answer: A

Q16. Candidate key is?
A. Minimal superkey
B. Non-key
C. FK
D. Duplicate
Correct Answer: B

Q17. Superkey is?
A. Minimal
B. Any unique-identifying set
C. Single attr
D. FK only
Correct Answer: A

Q18. Foreign key references?
A. Candidate
B. Primary of referenced
C. Any
D. Non-key
Correct Answer: B

Q19. Referential integrity prevents?
A. Duplicates
B. Dangling references
C. Null PK
D. Redundancy
Correct Answer: B

Q20. Entity integrity prevents?
A. Null PK
B. Duplicate FK
C. Null FK
D. Redundancy
Correct Answer: A

Q21. Functional dependency X->Y means?
A. X determines Y
B. Y determines X
C. Independent
D. Multivalued
Correct Answer: A

Q22. Trivial FD example?
A. AB->A
B. A->B
C. B->A
D. AB->C
Correct Answer: A

Q23. Armstrong axiom not included?
A. Reflexivity
B. Augmentation
C. Transitivity
D. Commutativity
Correct Answer: D

Q24. Closure of {A} with A->B,B->C is?
A. {A}
B. {A,B}
C. {A,B,C}
D. {C}
Correct Answer: C

Q25. R(A,B,C) F={A->B,B->C}. Candidate key?
A. A
B. B
C. C
D. AB
Correct Answer: C

Q26. R(A,B,C,D) F={AB->C,C->D,D->A}. Candidate key?
A. AB
B. C
C. D
D. B
Correct Answer: A

Q27. If A->B and B->A then?
A. Both keys
B. Equivalent
C. No key
D. Redundant
Correct Answer: B

Q28. Full FD vs partial: partial depends on?
A. Whole key
B. Part of key
C. Non-key
D. FK
Correct Answer: B

Q29. Transitive dependency is?
A. Non-key via another non-key
B. Key->key
C. Trivial
D. MVD
Correct Answer: A

Q30. 1NF requires?
A. No duplicates
B. Atomic values
C. No partial
D. No transitive
Correct Answer: B

Q31. Table with multivalued phone violates?
A. 1NF
B. 2NF
C. 3NF
D. BCNF
Correct Answer: A

Q32. 2NF removes?
A. Atomic
B. Partial dependency
C. Transitive
D. MVD
Correct Answer: B

Q33. Relation in 1NF with single-attr PK is automatically?
A. 1NF only
B. 2NF
C. 3NF
D. BCNF
Correct Answer: B

Q34. 3NF removes?
A. Partial
B. Transitive
C. MVD
D. Join dep
Correct Answer: B

Q35. BCNF condition: every determinant must be?
A. Non-key
B. Superkey
C. Prime
D. FK
Correct Answer: B

Q36. Every BCNF is in?
A. 1NF only
B. 3NF
C. 4NF
D. 5NF
Correct Answer: B

Q37. 3NF preserves dependencies but BCNF may not; true?
A. No
B. Yes
C. Both preserve
D. Neither
Correct Answer: B

Q38. 4NF removes?
A. Transitive
B. MVD
C. Partial
D. Join
Correct Answer: B

Q39. MVD X->->Y means?
A. FD
B. Independent multi-values
C. Key
D. Join
Correct Answer: B

Q40. 5NF deals with?
A. FD
B. Join dependency
C. MVD
D. Atomic
Correct Answer: B

Q41. Normalization goal?
A. More redundancy
B. Reduce redundancy/anomaly
C. Speed only
D. Indexing
Correct Answer: B

Q42. Insert anomaly due to?
A. Redundancy
B. Keys
C. Indexes
D. Views
Correct Answer: B

Q43. R(A,B,C) A->B, B->C. Highest normal form?
A. 1NF
B. 2NF
C. 3NF
D. BCNF
Correct Answer: B

Q44. R(A,B,C) A->B, A->C, key A. Normal form?
A. 1NF
B. 2NF
C. 3NF
D. BCNF
Correct Answer: D

Q45. R(A,B,C,D) AB->C, C->D. Violates?
A. 1NF
B. 2NF
C. 3NF/BCNF
D. 4NF
Correct Answer: B

Q46. Lossless join needs?
A. Common attr key in one
B. No common
C. All keys
D. MVD
Correct Answer: C

Q47. Lossy decomposition causes?
A. Extra tuples
B. Loss tuples
C. No change
D. Faster
Correct Answer: A

Q48. Dependency preservation means?
A. All FDs checkable without join
B. Lossless
C. BCNF
D. Keys preserved
Correct Answer: B

Q49. BCNF decomposition is always?
A. Lossless
B. Dependency preserving
C. Both
D. Neither
Correct Answer: A

Q50. 3NF synthesis is?
A. Lossless+preserving
B. Lossy
C. Not preserving
D. Redundant
Correct Answer: A

Q51. Canonical cover removes?
A. Redundant FDs/attrs
B. Keys
C. Tables
D. Indexes
Correct Answer: A

Q52. Extraneous attribute test uses?
A. Closure
B. Sampling
C. Index
D. View
Correct Answer: A

Q53. R(A,B) A->B, B->A. Normal form?
A. 1NF
B. 2NF
C. 3NF
D. BCNF
Correct Answer: D

Q54. Prime attribute is?
A. Part of any candidate key
B. Non-key
C. FK
D. Multivalued
Correct Answer: A

Q55. Non-prime determines prime violates?
A. 2NF possibly
B. 1NF
C. 4NF
D. 5NF
Correct Answer: A

Q56. Limitation of normalization: over-normalization causes?
A. More joins, slower queries
B. Faster always
C. Less storage always good
D. No joins
Correct Answer: B

Q57. Denormalization used for?
A. OLTP purity
B. OLAP/read performance
C. Security
D. Integrity
Correct Answer: B

Q58. SQL full form?
A. Structured Query Language
B. Simple Query
C. Sequential
D. Standard Question
Correct Answer: B

Q59. DDL includes?
A. SELECT
B. CREATE/ALTER/DROP
C. GRANT
D. INSERT
Correct Answer: B

Q60. DML includes?
A. CREATE
B. SELECT/INSERT/UPDATE/DELETE
C. GRANT
D. REVOKE
Correct Answer: B

Q61. DCL includes?
A. SELECT
B. GRANT/REVOKE
C. ALTER
D. DELETE
Correct Answer: B

Q62. TCL includes?
A. COMMIT/ROLLBACK
B. CREATE
C. GRANT
D. SELECT
Correct Answer: B

Q63. CREATE TABLE belongs to?
A. DML
B. DDL
C. DCL
D. TCL
Correct Answer: B

Q64. DROP vs TRUNCATE: TRUNCATE?
A. Removes structure
B. Removes rows, keeps structure, no rollback in some DBs
C. Same as DELETE
D. DCL
Correct Answer: B

Q65. DELETE vs TRUNCATE: DELETE?
A. DDL
B. DML with WHERE, logged
C. No log
D. Drops table
Correct Answer: B

Q66. ALTER ADD COLUMN is?
A. DML
B. DDL
C. DCL
D. TCL
Correct Answer: B

Q67. Data types: VARCHAR vs CHAR?
A. Same
B. VARCHAR variable, CHAR fixed padded
C. CHAR variable
D. Both numeric
Correct Answer: B

Q68. NUMBER(10,2) means?
A. 10 digits 2 decimal
B. 10 rows
C. 2 tables
D. Exponent
Correct Answer: A

Q69. DATE default includes?
A. Time only
B. Date (+time)
C. String
D. Integer
Correct Answer: B

Q70. Constraint NOT NULL is?
A. Column
B. Table
C. FK
D. Check
Correct Answer: A

Q71. UNIQUE allows?
A. Duplicates
B. One null (Oracle) / multiple (SQL Server), no duplicates
C. Null PK
D. FK
Correct Answer: B

Q72. CHECK constraint validates?
A. Uniqueness
B. Predicate
C. FK
D. PK
Correct Answer: B

Q73. DEFAULT sets?
A. Null always
B. Value if not provided
C. PK
D. Index
Correct Answer: A

Q74. CREATE VIEW syntax correct?
A. CREATE VIEW v AS SELECT...
B. CREATE TABLE v
C. MAKE VIEW
D. VIEW CREATE
Correct Answer: B

Q75. SELECT DISTINCT removes?
A. Nulls
B. Duplicates
C. Table
D. Index
Correct Answer: B

Q76. WHERE vs HAVING: HAVING filters?
A. Rows
B. Groups after GROUP BY
C. Tables
D. Columns
Correct Answer: A

Q77. GROUP BY used with?
A. Aggregates
B. ORDER only
C. JOIN only
D. Subquery only
Correct Answer: B

Q78. COUNT(*) vs COUNT(col): latter?
A. Counts nulls
B. Ignores nulls
C. Same
D. Counts tables
Correct Answer: A

Q79. Output of SELECT 'A'||'B' in Oracle?
A. A
B. B
C. AB
D. Error
Correct Answer: C

Q80. LIKE 'A%' matches?
A. Starts with A
B. Ends with A
C. Contains A
D. Exactly A
Correct Answer: A

Q81. LIKE '_abc' matches how many chars + abc?
A. 0
B. 1
C. Many
D. None
Correct Answer: B

Q82. BETWEEN 10 AND 20 inclusive?
A. Yes
B. Exclusive
C. Only 10
D. Only 20
Correct Answer: A

Q83. IN vs EXISTS: EXISTS checks?
A. List
B. Existence, correlated
C. Equality
D. Null
Correct Answer: B

Q84. ORDER BY 2 means?
A. Second column
B. Value 2
C. Two rows
D. Desc
Correct Answer: B

Q85. ORDER BY default?
A. DESC
B. ASC
C. Random
D. Grouped
Correct Answer: B

Q86. Aggregate without GROUP BY returns?
A. Many rows
B. Single row
C. Zero
D. Error
Correct Answer: B

Q87. WHERE age IS NULL correct?
A. = NULL
B. IS NULL
C. LIKE NULL
D. IN NULL
Correct Answer: B

Q88. SELECT NVL(NULL,5) returns?
A. NULL
B. 5
C. 0
D. Error
Correct Answer: B

Q89. JOIN without ON results in?
A. Inner
B. Cartesian
C. Outer
D. Error always
Correct Answer: B

Q90. INNER JOIN returns?
A. All left
B. Matching only
C. All both + nulls
D. Cross
Correct Answer: B

Q91. LEFT OUTER JOIN returns?
A. Matching + unmatched left
B. Right only
C. Matching only
D. None
Correct Answer: A

Q92. FULL OUTER JOIN returns?
A. Matching only
B. Both unmatched + matched
C. Left only
D. Cross
Correct Answer: B

Q93. SELF JOIN needs?
A. Two tables
B. Aliases
C. View
D. Index
Correct Answer: B

Q94. EQUIJOIN uses?
A. =
B. >
C. BETWEEN
D. LIKE
Correct Answer: A

Q95. NATURAL JOIN joins on?
A. All same-name cols
B. PK only
C. FK only
D. First col
Correct Answer: A

Q96. Subquery in WHERE with > ALL means?
A. Greater than max
B. Greater than min
C. Equal
D. In list
Correct Answer: B

Q97. > ANY means?
A. Greater than max
B. Greater than min (at least one)
C. Equal all
D. None
Correct Answer: A

Q98. Correlated subquery executes?
A. Once
B. Per outer row
C. Never
D. After
Correct Answer: B

Q99. Output: SELECT 10/3 in integer DB?
A. 3
B. 3.33
C. 3.0
D. Error
Correct Answer: A

Q100. Output: SELECT MOD(10,3)?
A. 3
B. 1
C. 0
D. 10
Correct Answer: B

Q101. UNION vs UNION ALL: UNION?
A. Keeps duplicates
B. Removes duplicates, sorts
C. No sort
D. Intersect
Correct Answer: B

Q102. INTERSECT returns?
A. Union
B. Common
C. Difference
D. Cartesian
Correct Answer: B

Q103. MINUS/EXCEPT returns?
A. Common
B. In first not second
C. Union
D. Join
Correct Answer: B

Q104. UNION column requirement?
A. Same number/type-compatible
B. Any
C. Same name
D. Same key
Correct Answer: A

Q105. ORDER BY in UNION placed?
A. Each query
B. At end
C. First only
D. Not allowed
Correct Answer: B

Q106. INSERT without column list needs?
A. Partial values
B. All columns order
C. No values
D. Defaults only
Correct Answer: B

Q107. INSERT INTO ... SELECT does?
A. Create table
B. Bulk copy
C. Delete
D. Update
Correct Answer: B

Q108. UPDATE without WHERE?
A. No rows
B. All rows
C. Error
D. First row
Correct Answer: B

Q109. DELETE without WHERE?
A. Drops table
B. Deletes all rows
C. Error
D. No effect
Correct Answer: B

Q110. MERGE statement does?
A. Insert only
B. Upsert (insert/update)
C. Delete only
D. Join only
Correct Answer: B

Q111. GRANT SELECT ON t TO user is?
A. DDL
B. DCL
C. DML
D. TCL
Correct Answer: B

Q112. REVOKE removes?
A. Table
B. Privilege
C. Row
D. Index
Correct Answer: B

Q113. Role is?
A. Table
B. Privilege bundle
C. User
D. View
Correct Answer: B

Q114. WITH GRANT OPTION allows?
A. Revoke
B. Further grant
C. Delete table
D. Create DB
Correct Answer: B

Q115. COMMIT makes?
A. Undo
B. Permanent
C. Temporary
D. Lock
Correct Answer: B

Q116. ROLLBACK undoes?
A. Committed
B. Uncommitted
C. DDL always
D. Grant
Correct Answer: B

Q117. SAVEPOINT allows?
A. Full commit
B. Partial rollback
C. Lock
D. Index
Correct Answer: B

Q118. ACID: Atomicity ensured by?
A. Log/undo-redo
B. Locks
C. Timestamp
D. Index
Correct Answer: A

Q119. Consistency ensured by?
A. Recovery only
B. Integrity constraints + app
C. Locks
D. Deadlock
Correct Answer: B

Q120. Isolation levels: lowest?
A. Serializable
B. Read uncommitted
C. Repeatable read
D. Read committed
Correct Answer: B

Q121. Dirty read allowed in?
A. Read uncommitted
B. Serializable
C. Repeatable
D. Read committed
Correct Answer: A

Q122. Phantom prevented in?
A. Read uncommitted
B. Serializable
C. Read committed
D. None
Correct Answer: B

Q123. View is?
A. Physical table
B. Virtual/stored query
C. Index
D. Sequence
Correct Answer: B

Q124. Updatable view requires?
A. Join/group
B. Single table, no aggregate/distinct
C. Aggregate
D. UNION
Correct Answer: B

Q125. WITH CHECK OPTION ensures?
A. Performance
B. DML via view satisfies view predicate
C. Read only
D. Index
Correct Answer: B

Q126. Materialized view stores?
A. Query only
B. Data, refreshed
C. Index
D. Log
Correct Answer: B

Q127. Index improves?
A. Write speed
B. Read/selective queries
C. Storage
D. Redundancy
Correct Answer: B

Q128. Index overhead?
A. None
B. Storage + slower writes
C. Faster writes
D. No maintenance
Correct Answer: B

Q129. B-tree index good for?
A. Range queries
B. Exact only
C. Hash only
D. Full scan
Correct Answer: A

Q130. Bitmap index good for?
A. High cardinality OLTP
B. Low cardinality DW
C. Range
D. Text
Correct Answer: B

Q131. Unique index ensures?
A. Duplicates
B. Uniqueness
C. Nulls
D. FK
Correct Answer: B

Q132. Composite index (A,B) helps WHERE B=? alone?
A. Yes fully
B. Typically not (leftmost)
C. Always
D. Never any
Correct Answer: B

Q133. Clustered index order?
A. Unordered
B. Physical row order
C. Logical only
D. Hash
Correct Answer: B

Q134. CREATE INDEX is?
A. DML
B. DDL
C. DCL
D. TCL
Correct Answer: B

Q135. Sequence generates?
A. Random
B. Unique numbers
C. Strings
D. Dates
Correct Answer: B

Q136. NEXTVAL vs CURRVAL: CURRVAL needs?
A. Nothing
B. NEXTVAL first in session
C. Commit
D. Rollback
Correct Answer: B

Q137. Sequence gap due to?
A. Rollback/cache
B. Commit
C. Index
D. View
Correct Answer: A

Q138. Synonym is?
A. Copy
B. Alias for object
C. Duplicate table
D. Index
Correct Answer: B

Q139. Data dictionary stores?
A. User data
B. Metadata
C. Logs
D. Indexes only
Correct Answer: B

Q140. USER_TABLES vs ALL_TABLES vs DBA_TABLES differ by?
A. Size
B. Scope/privilege
C. Speed
D. Type
Correct Answer: B

Q141. Primary key automatically creates?
A. View
B. Index
C. Sequence
D. Synonym
Correct Answer: B

Q142. Foreign key creates index automatically? (Oracle)
A. Yes always
B. No, must create
C. Yes in all DBs
D. Creates view
Correct Answer: B

Q143. Query: SELECT COUNT(*) FROM emp WHERE dept=10; with 0 rows returns?
A. 0 rows
B. 0 (single row)
C. NULL
D. Error
Correct Answer: B

Q144. Query: SELECT SUM(sal) with all NULL returns?
A. 0
B. NULL
C. Error
D. 1
Correct Answer: B

Q145. GROUP BY dept HAVING COUNT(*)>5 filters?
A. Rows
B. Groups
C. Columns
D. Tables
Correct Answer: B

Q146. WHERE sal > (SELECT AVG(sal) FROM emp) is?
A. Correlated
B. Non-correlated aggregate subquery
C. Join
D. Union
Correct Answer: B

Q147. Second highest salary query uses?
A. MAX
B. Subquery < MAX or DENSE_RANK
C. MIN
D. COUNT
Correct Answer: B

Q148. DENSE_RANK vs RANK: DENSE?
A. Gaps
B. No gaps
C. Same
D. Row_number
Correct Answer: B

Q149. DELETE duplicate rows technique?
A. DISTINCT in delete
B. ROWID/min(rowid)
C. Index
D. View
Correct Answer: A

Q150. Query flattening is?
A. Optimizer transform
B. Normalization
C. Index
D. View
Correct Answer: B

Q151. Explain plan shows?
A. Data
B. Execution plan
C. Dictionary
D. Locks
Correct Answer: B

Q152. Cost-based optimizer uses?
A. Rules only
B. Statistics
C. Random
D. User hint only
Correct Answer: B

Q153. Selectivity low means?
A. Many rows
B. Few rows, index useful
C. All rows
D. No rows
Correct Answer: B

Q154. Join order affects?
A. Result
B. Performance
C. Correctness
D. Keys
Correct Answer: B

Q155. Nested-loop join best for?
A. Large-large
B. Small-outer, indexed inner
C. No index
D. Cartesian
Correct Answer: B

Q156. Hash join best for?
A. Small tables
B. Large equijoin, no index
C. Range
D. Sorted
Correct Answer: B

Q157. Sort-merge needs?
A. Hash
B. Sorted inputs
C. Index only
D. Small
Correct Answer: B

Q158. Transaction schedule serializable if?
A. Conflict-equivalent to serial
B. Has dirty read
C. Concurrent
D. Locked
Correct Answer: A

Q159. Conflict operations are?
A. Read-read
B. Read-write/write-write same item
C. Write-read diff
D. Commit
Correct Answer: B

Q160. Precedence graph cycle means?
A. Serializable
B. Not serializable
C. Deadlock
D. Recoverable
Correct Answer: B

Q161. Two-phase locking ensures?
A. Deadlock free
B. Serializability
C. No starvation
D. Recovery
Correct Answer: B

Q162. Strict 2PL holds locks till?
A. Growing
B. Commit/abort
C. Shrinking early
D. Start
Correct Answer: B

Q163. Deadlock prevention: wait-die uses?
A. Age/priority
B. Timeout only
C. Detection
D. No timestamps
Correct Answer: A

Q164. Deadlock detection uses?
A. Wait-for graph
B. Precedence
C. Lock table only
D. Log
Correct Answer: A

Q165. Timestamp ordering uses?
A. Locks only
B. Timestamps for order
C. 2PL
D. Graph
Correct Answer: B

Q166. Thomas write rule ignores?
A. Late reads
B. Obsolete writes
C. Early writes
D. Commits
Correct Answer: B

Q167. Recoverable schedule: commit after?
A. Readers commit
B. Read-from writers commit
C. Abort
D. Start
Correct Answer: B

Q168. Cascadeless means?
A. No dirty reads
B. No aborts
C. No commits
D. No locks
Correct Answer: B

Q169. Log-based recovery uses?
A. Indexes
B. Undo/redo
C. Shadows only
D. Checkpoints only
Correct Answer: B

Q170. Checkpoint reduces?
A. Locks
B. Recovery time
C. Deadlock
D. Serializability
Correct Answer: B

Q171. Shadow paging uses?
A. Log
B. Two page tables
C. Locks
D. Timestamps
Correct Answer: B

Q172. SQL injection prevented by?
A. Concatenation
B. Bind variables/prepared
C. Dynamic
D. Grant all
Correct Answer: B

Q173. Privilege to create table?
A. CONNECT
B. RESOURCE/CREATE TABLE
C. DBA only
D. SELECT
Correct Answer: B

Q174. PUBLIC grant means?
A. One user
B. All users
C. Admin
D. Role
Correct Answer: B

Q175. View for security hides?
A. All data
B. Sensitive cols/rows
C. Indexes
D. Keys
Correct Answer: B

Q176. Assertion is?
A. Table constraint
B. DB-wide predicate
C. View
D. Index
Correct Answer: B

Q177. Trigger fires on?
A. SELECT always
B. Insert/update/delete events
C. Commit
D. Grant
Correct Answer: B

Q178. Row vs statement trigger: row fires?
A. Once per statement
B. Per row
C. Once per DB
D. On select
Correct Answer: B

Q179. BEFORE vs AFTER trigger: BEFORE for?
A. Logging
B. Validation/modify new
C. Audit
D. Commit
Correct Answer: B

Q180. Instead-of trigger on?
A. Tables
B. Views
C. Indexes
D. Sequences
Correct Answer: B

Q181. Stored procedure vs function: function?
A. No return
B. Returns value, callable in SQL
C. No params
D. TCL only
Correct Answer: B

Q182. Cursor is for?
A. Set processing
B. Row-by-row
C. DDL
D. Index
Correct Answer: B

Q183. Embedded SQL uses?
A. API
B. Precompiler/host vars
C. Trigger
D. View
Correct Answer: B

Q184. Closure test: X+ with F={AB->C,C->D}. (AB)+?
A. AB
B. ABC
C. ABCD
D. ABD
Correct Answer: C

Q185. Minimal cover of {A->B,B->C,A->C}?
A. Same
B. A->B,B->C
C. A->C
D. B->A
Correct Answer: B

Q186. R(A,B,C,D,E) F={A->B,B->C,C->D,D->E}. Key?
A. A
B. B
C. E
D. AB
Correct Answer: A

Q187. Decomposition R1(A,B),R2(B,C) from R(A,B,C) with A->B,B->C lossless?
A. Yes
B. No
C. Depends
D. Lossy? Check B key in R2 yes lossless
Correct Answer: A

Q188. FD preserved if union closures equal; tool is?
A. Chase
B. Closure comparison
C. Graph
D. Index
Correct Answer: B

Q189. R(A,B,C) F={AB->C,C->A}. Keys?
A. AB only
B. AB and BC
C. C
D. A
Correct Answer: B

Q190. Highest NF of Q189?
A. 1NF
B. 2NF
C. 3NF
D. BCNF? C->A with C not superkey violates BCNF but 3NF holds as A prime
Correct Answer: C

Q191. Query: SELECT * FROM t WHERE col=NULL returns?
A. Null rows
B. Zero (use IS NULL)
C. All
D. Error
Correct Answer: B

Q192. COUNT DISTINCT col ignores?
A. Duplicates+nulls
B. All
C. Only duplicates
D. None
Correct Answer: A

Q193. FK ON DELETE CASCADE does?
A. Block delete
B. Delete children
C. Nullify
D. Nothing
Correct Answer: B

Q194. ON DELETE SET NULL requires?
A. Not null FK
B. Nullable FK
C. PK
D. Unique
Correct Answer: B

Q195. Deferrable constraint checked at?
A. Row time
B. Commit
C. Start
D. Grant
Correct Answer: B

Q196. Domain constraint example?
A. PK
B. CHECK age>0
C. FK
D. Index
Correct Answer: B

Q197. NULL in UNIQUE + FK semantics tricky; true?
A. No
B. Yes, nulls not equal/comparable
C. Always error
D. Ignore
Correct Answer: B

Q198. Three-valued logic: NULL AND FALSE =?
A. TRUE
B. FALSE
C. UNKNOWN
D. NULL only
Correct Answer: B

Q199. NULL OR TRUE =?
A. FALSE
B. TRUE
C. UNKNOWN
D. NULL
Correct Answer: B

Q200. Best candidate key choice heuristic?
A. Longest
B. Minimal, stable, numeric/surrogate
C. Nullable
D. Composite always
Correct Answer: B

---
## ANSWER KEY
1-A 2-B 3-B 4-B 5-B 6-B 7-B 8-B 9-B 10-A
11-B 12-A 13-A 14-B 15-A 16-B 17-A 18-B 19-B 20-A
21-A 22-A 23-D 24-C 25-C 26-A 27-B 28-B 29-A 30-B
31-A 32-B 33-B 34-B 35-B 36-B 37-B 38-B 39-B 40-B
41-B 42-B 43-B 44-D 45-B 46-C 47-A 48-B 49-A 50-A
51-A 52-A 53-D 54-A 55-A 56-B 57-B 58-B 59-B 60-B
61-B 62-B 63-B 64-B 65-B 66-B 67-B 68-A 69-B 70-A
71-B 72-B 73-A 74-B 75-B 76-A 77-B 78-A 79-C 80-A
81-B 82-A 83-B 84-B 85-B 86-B 87-B 88-B 89-B 90-B
91-A 92-B 93-B 94-A 95-A 96-B 97-A 98-B 99-A 100-B
101-B 102-B 103-B 104-A 105-B 106-B 107-B 108-B 109-B 110-B
111-B 112-B 113-B 114-B 115-B 116-B 117-B 118-A 119-B 120-B
121-A 122-B 123-B 124-B 125-B 126-B 127-B 128-B 129-A 130-B
131-B 132-B 133-B 134-B 135-B 136-B 137-A 138-B 139-B 140-B
141-B 142-B 143-B 144-B 145-B 146-B 147-B 148-B 149-A 150-B
151-B 152-B 153-B 154-B 155-B 156-B 157-B 158-A 159-B 160-B
161-B 162-B 163-A 164-A 165-B 166-B 167-B 168-B 169-B 170-B
171-B 172-B 173-B 174-B 175-B 176-B 177-B 178-B 179-B 180-B
181-B 182-B 183-B 184-C 185-B 186-A 187-A 188-B 189-B 190-C
191-B 192-A 193-B 194-B 195-B 196-B 197-B 198-B 199-B 200-B
