# Topic 9: System Software & Compilers

**Syllabus:** 8085 assembly fundamentals, assemblers (2-pass/single-pass), macros, loader/linker (loading/linking/relocation/relocatability/linkage editing), text editors/debuggers, compilation vs interpretation, bootstrap, phases of compilation, lexical analysis/Lex, CFG/parsing/parse trees/leftmost-rightmost derivations, bottom-up (shift-reduce/operator precedence/LR)/YACC, top-down (left recursion removal/recursive descent/predictive), intermediate codes (quadruples/triples), code generation & optimization.

Q1. Which register in 8085 is used as accumulator?
A. A
B. B
C. H
D. SP
Correct Answer: A

Q2. Size of accumulator in 8085 is:
A. 4-bit
B. 8-bit
C. 16-bit
D. 32-bit
Correct Answer: B

Q3. 8085 has how many general purpose 8-bit registers?
A. 4
B. 5
C. 6
D. 7
Correct Answer: A

Q4. Which pair forms the 16-bit HL register pair?
A. H and L
B. B and C
C. D and E
D. A and F
Correct Answer: A

Q5. Program Counter in 8085 is:
A. 8-bit
B. 16-bit
C. 20-bit
D. 32-bit
Correct Answer: B

Q6. Stack Pointer in 8085 is:
A. 8-bit
B. 16-bit
C. 6-bit
D. 4-bit
Correct Answer: B

Q7. Number of flags in 8085 flag register used is:
A. 4
B. 5
C. 8
D. 16
Correct Answer: B

Q8. Which is NOT a flag in 8085?
A. Overflow
B. Zero
C. Carry
D. Parity
Correct Answer: A

Q9. HLT instruction in 8085 means:
A. Halt processor
B. Hold bus
C. High level transfer
D. Hardware trap
Correct Answer: A

Q10. NOP instruction performs:
A. No operation
B. Normal output pulse
C. Next operation
D. Null pointer
Correct Answer: A

Q11. LDA instruction in 8085 is:
A. Load accumulator direct
B. Load accumulator indirect
C. Logical AND
D. Long address
Correct Answer: A

Q12. STA instruction stores:
A. Accumulator to memory
B. Stack to accumulator
C. Status to accumulator
D. Stack to memory
Correct Answer: A

Q13. MOV A,B means:
A. Copy B to A
B. Copy A to B
C. Add B to A
D. Move memory to bus
Correct Answer: A

Q14. ADD B instruction adds:
A. B to accumulator
B. B to H
C. B to stack
D. B to PC
Correct Answer: A

Q15. INR M means:
A. Increment memory pointed by HL
B. Increment microprocessor
C. Input from memory
D. Interrupt memory
Correct Answer: A

Q16. DCR C means:
A. Decrement C by 1
B. Decode C
C. Divide by C
D. Direct call
Correct Answer: A

Q17. JMP instruction is:
A. Unconditional jump
B. Jump if zero
C. Jump if carry
D. Jump subroutine
Correct Answer: A

Q18. JZ jumps when:
A. Zero flag=1
B. Carry=1
C. Sign=0
D. Parity=1
Correct Answer: A

Q19. CALL instruction:
A. Calls subroutine, saves return address on stack
B. Calls interrupt only
C. Copies accumulator to stack
D. Clears accumulator
Correct Answer: A

Q20. RET returns from:
A. Subroutine
B. Interrupt only
C. Halt
D. Reset
Correct Answer: A

Q21. PUSH B pushes:
A. BC pair onto stack
B. B only
C. Accumulator only
D. PC only
Correct Answer: A

Q22. POP H pops:
A. Top of stack to HL
B. HL to stack
C. H only
D. Hold state
Correct Answer: A

Q23. XCHG exchanges:
A. HL with DE
B. A with B
C. PC with SP
D. H with L
Correct Answer: A

Q24. 8085 address bus is:
A. 8-bit
B. 16-bit
C. 20-bit
D. 32-bit
Correct Answer: B

Q25. 8085 data bus is:
A. 8-bit
B. 16-bit
C. 32-bit
D. 4-bit
Correct Answer: A

Q26. 8085 can address memory:
A. 64KB
B. 4KB
C. 1MB
D. 16KB
Correct Answer: A

Q27. Which addressing mode is MVI A,05H?
A. Immediate
B. Direct
C. Register indirect
D. Implied
Correct Answer: A

Q28. Which addressing mode is LDA 2000H?
A. Direct
B. Immediate
C. Register
D. Implicit
Correct Answer: A

Q29. Which is register indirect?
A. MOV A,M
B. MVI A,05
C. LDA 2000
D. CMA
Correct Answer: A

Q30. CMA instruction:
A. Complement accumulator
B. Clear memory
C. Compare accumulator
D. Call memory
Correct Answer: A

Q31. Main function of assembler is to:
A. Translate assembly to machine code
B. Translate high-level to assembly
C. Load program into memory
D. Debug program
Correct Answer: A

Q32. Two-pass assembler performs:
A. Pass1 builds symbol table, Pass2 generates code
B. Both passes generate code
C. Pass1 executes, Pass2 assembles
D. Pass1 loads, Pass2 links
Correct Answer: A

Q33. In Pass1 of two-pass assembler, MOT stands for:
A. Mnemonic Operation Table
B. Memory Operation Table
C. Machine Output Table
D. Macro Operation Table
Correct Answer: A

Q34. POT stands for:
A. Pseudo-Operation Table
B. Program Operation Table
C. Pass Operation Table
D. Print Operation Table
Correct Answer: A

Q35. Symbol Table stores:
A. Symbols and addresses/values
B. Only opcodes
C. Only macros
D. Object code
Correct Answer: A

Q36. Literal Table stores:
A. Literals and addresses
B. Symbols only
C. Macros only
D. Errors
Correct Answer: A

Q37. Forward reference problem is solved by:
A. Two-pass assembler
B. Single-pass with backpatching only always fails
C. Compiler
D. Loader
Correct Answer: A

Q38. Single-pass assembler handles forward reference by:
A. Backpatching / fix-ups
B. Ignoring
C. Two symbol tables
D. Halting
Correct Answer: A

Q39. Pseudo-ops are:
A. Assembler directives, no machine code
B. Machine instructions
C. Macros
D. Executable instructions
Correct Answer: A

Q40. Example of pseudo-op:
A. START, END, EQU, DS
B. ADD, SUB
C. LDA, STA
D. JMP, CALL
Correct Answer: A

Q41. EQU pseudo-op is used to:
A. Equate symbol to value
B. Equalize registers
C. End program
D. Erase memory
Correct Answer: A

Q42. ORIGIN/START directive specifies:
A. Starting address
B. End address
C. Stack size
D. Macro start
Correct Answer: A

Q43. Base table in assembler is used for:
A. Relocation
B. Macro expansion
C. Lexical analysis
D. Debugging
Correct Answer: A

Q44. Cross assembler is one that:
A. Runs on one machine, generates code for another
B. Runs cross-platform UI
C. Assembles two programs
D. Needs two passes on cross memory
Correct Answer: A

Q45. One-pass assembler is suitable for:
A. Systems with limited memory / single scan
B. Only high-level languages
C. No symbols
D. No literals
Correct Answer: A

Q46. Pass2 of assembler uses:
A. Symbol/Literal tables + MOT/POT to generate object code
B. Only source
C. Only object
D. Linker output
Correct Answer: A

Q47. Intermediate file between Pass1 and Pass2 contains:
A. Intermediate code with addresses
B. Final executable
C. High-level code
D. Debug info only
Correct Answer: A

Q48. Load-and-go assembler:
A. Generates code directly in memory for execution, no object file
B. Needs loader always
C. Generates high-level code
D. Requires linkage editor
Correct Answer: A

Q49. Which error is detected in Pass1?
A. Undefined symbol / duplicate symbol
B. Runtime divide by zero
C. Logic error
D. Deadlock
Correct Answer: A

Q50. Which error is detected in Pass2?
A. Invalid opcode / addressability
B. Syntax of macro definition always
C. Deadlock
D. Page fault
Correct Answer: A

Q51. Macro definition uses directives:
A. MACRO and MEND
B. START and END
C. CALL and RETURN
D. PUSH and POP
Correct Answer: A

Q52. Macro call causes:
A. Expansion
B. Condensation
C. Compilation
D. Loading
Correct Answer: A

Q53. Macro processor expands:
A. Before assembly
B. After loading
C. During execution
D. After linking
Correct Answer: A

Q54. Positional parameters in macros are distinguished by:
A. Position
B. Keyword name
C. Type
D. Value range
Correct Answer: A

Q55. Keyword parameters are distinguished by:
A. Name
B. Position only
C. Address
D. Opcode
Correct Answer: A

Q56. Nested macro calls mean:
A. Macro calls another macro
B. Macro calls itself only
C. Two assemblers
D. Recursive loader
Correct Answer: A

Q57. MDT stands for:
A. Macro Definition Table
B. Memory Definition Table
C. Mnemonic Definition Table
D. Machine Data Table
Correct Answer: A

Q58. MNT stands for:
A. Macro Name Table
B. Memory Name Table
C. Machine Name Table
D. Mnemonic Name Table
Correct Answer: A

Q59. ALA stands for in macro processing:
A. Argument List Array
B. Address List Array
C. Assembler List Array
D. Allocation Array
Correct Answer: A

Q60. Conditional macro expansion uses:
A. IF/ELSE/ENDIF in macro
B. JMP only
C. Loader condition
D. Interrupt
Correct Answer: A

Q61. Function of loader is to:
A. Load program into memory for execution
B. Translate source
C. Edit text
D. Optimize code
Correct Answer: A

Q62. Absolute loader loads program at:
A. Fixed address, no relocation
B. Any address with relocation
C. Virtual address only
D. Cache only
Correct Answer: A

Q63. Relocating loader allows:
A. Loading at different addresses via relocation
B. Only fixed address
C. No address translation
D. Only overlays
Correct Answer: A

Q64. Relocation is needed when:
A. Program loaded at address different from assembled
B. Program has no symbols
C. No linker used
D. Macro used
Correct Answer: A

Q65. Relocatability is ability to:
A. Execute from different memory locations
B. Relocate files on disk
C. Move compiler
D. Reboot OS
Correct Answer: A

Q66. Linker combines:
A. Object modules into executable
B. Source files into assembly
C. Macros into tables
D. Pages into frames
Correct Answer: A

Q67. Linkage editing includes:
A. Resolving external symbols and address adjustment
B. Editing source text
C. Compiling functions
D. Debugging
Correct Answer: A

Q68. External symbol resolution is done by:
A. Linker
B. Text editor
C. Debugger
D. Lexer
Correct Answer: A

Q69. Static linking occurs:
A. Before execution
B. During execution on demand
C. At runtime by OS
D. In CPU
Correct Answer: A

Q70. Dynamic linking occurs:
A. At runtime / load time
B. During assembly
C. During macro expansion
D. During editing
Correct Answer: A

Q71. Binder is another name for:
A. Linker
B. Loader
C. Assembler
D. Compiler
Correct Answer: A

Q72. Overlay structure is used when:
A. Program larger than memory
B. Program smaller than memory
C. No I/O
D. No linker
Correct Answer: A

Q73. Bootstrap loader is:
A. Small program to load OS kernel
B. Compiler starter
C. Macro loader
D. Text formatter
Correct Answer: A

Q74. Text editor provides:
A. Create/modify source files
B. Execute programs
C. Allocate memory
D. Schedule CPU
Correct Answer: A

Q75. Debugger allows:
A. Breakpoints, step execution, watch variables
B. Only editing
C. Only compiling
D. Only loading
Correct Answer: A

Q76. Compiler translates:
A. High-level to machine/object code in one go before execution
B. Line by line during execution
C. Assembly to high-level
D. Object to source
Correct Answer: A

Q77. Interpreter:
A. Executes source line by line without producing object file
B. Produces exe before execution
C. Links modules
D. Loads OS
Correct Answer: A

Q78. Compiled programs generally:
A. Have faster execution
B. Have slower execution
C. No optimization possible
D. Always portable
Correct Answer: A

Q79. Bootstrap in compilers means:
A. Writing compiler in its own language using minimal initial compiler
B. Booting OS
C. Loading assembler
D. Starting debugger
Correct Answer: A

Q80. T-diagrams represent:
A. Compiler bootstrapping relationships
B. Memory layout
C. Parse trees
D. Deadlock
Correct Answer: A

Q81. Cross-compiler generates code for:
A. Different machine than host
B. Same machine only
C. Human reading
D. Interpreter only
Correct Answer: A

Q82. Decompiler converts:
A. Machine/object to high-level
B. High-level to machine
C. Assembly to macro
D. Text to binary
Correct Answer: A

Q83. First phase of compilation is:
A. Lexical analysis
B. Code generation
C. Optimization
D. Syntax analysis
Correct Answer: A

Q84. Last phase of compilation is:
A. Code generation
B. Lexical analysis
C. Parsing
D. Semantic analysis
Correct Answer: A

Q85. Correct order of phases is:
A. Lexical-Syntax-Semantic-ICG-Optimization-CodeGen
B. Syntax-Lexical-CodeGen-Optimization
C. Semantic-Lexical-Syntax-CodeGen
D. CodeGen-Lexical-Syntax-Semantic
Correct Answer: A

Q86. Lexical analysis converts:
A. Source characters to tokens
B. Tokens to parse tree
C. Parse tree to IC
D. IC to object
Correct Answer: A

Q87. Tool Lex generates:
A. Lexical analyzer
B. Parser
C. Code generator
D. Loader
Correct Answer: A

Q88. Input to Lex is:
A. Regular expressions / patterns with actions
B. CFG
C. Quadruples
D. Object code
Correct Answer: A

Q89. Output of Lex is typically:
A. C program for scanner (lex.yy.c)
B. Assembly file
C. EXE
D. Parse table
Correct Answer: A

Q90. Token is:
A. Sequence of characters with collective meaning (identifier, keyword)
B. Single character only
C. Parse tree
D. Grammar rule
Correct Answer: A

Q91. Lexeme is:
A. Actual character sequence forming token
B. Token type
C. Grammar
D. Symbol table entry only
Correct Answer: A

Q92. Pattern describes:
A. Rule for lexemes of a token (via regex)
B. Parse tree shape
C. Object layout
D. Memory map
Correct Answer: A

Q93. Which handles whitespace/comments?
A. Lexical analyzer (usually skips)
B. Code generator
C. Optimizer
D. Linker
Correct Answer: A

Q94. Longest match rule in Lex means:
A. Longest possible lexeme preferred
B. Shortest preferred
C. First rule always
D. Random
Correct Answer: A

Q95. Symbol table is used in:
A. All phases
B. Only code gen
C. Only linking
D. Only editing
Correct Answer: A

Q96. CFG stands for:
A. Context-Free Grammar
B. Combined Formal Grammar
C. Code Flow Graph
D. Control Flow Grammar
Correct Answer: A

Q97. CFG consists of:
A. Terminals, Non-terminals, Productions, Start symbol
B. Only terminals
C. Only tokens
D. Frames and pages
Correct Answer: A

Q98. Parse tree shows:
A. Derivation structure of string per grammar
B. Memory allocation
C. Symbol table
D. Flowchart
Correct Answer: A

Q99. Leftmost derivation expands:
A. Leftmost non-terminal first
B. Rightmost first
C. Random
D. All at once
Correct Answer: A

Q100. Rightmost derivation expands:
A. Rightmost non-terminal first
B. Leftmost first
C. Terminals first
D. All at once
Correct Answer: A

Q101. Rightmost derivation in reverse corresponds to:
A. Bottom-up parsing
B. Top-down parsing
C. Lexical analysis
D. Code optimization
Correct Answer: A

Q102. Leftmost derivation corresponds to:
A. Top-down parsing
B. Bottom-up parsing
C. Code gen
D. Linking
Correct Answer: A

Q103. Ambiguous grammar has:
A. More than one parse tree for a string
B. No parse tree
C. Exactly one leftmost derivation
D. No terminals
Correct Answer: A

Q104. Which grammar is suitable for deterministic parsing?
A. Unambiguous
B. Ambiguous
C. Regular only never CFG
D. Type-0 only
Correct Answer: A

Q105. Sentence of grammar is:
A. String of terminals derivable from start
B. Any production
C. Any non-terminal
D. Token stream only
Correct Answer: A

Q106. Sentential form may contain:
A. Terminals and non-terminals
B. Only terminals
C. Only start symbol
D. Object code
Correct Answer: A

Q107. Handle in bottom-up parsing is:
A. Substring matching RHS to reduce
B. Leftmost token
C. Symbol table handle
D. File handle
Correct Answer: A

Q108. Shift-reduce parsing actions are:
A. Shift, Reduce, Accept, Error
B. Push, Pop only
C. Lex, Yacc
D. Load, Store
Correct Answer: A

Q109. Shift means:
A. Push input symbol onto stack
B. Pop stack to output
C. Replace RHS with LHS
D. Discard stack
Correct Answer: A

Q110. Reduce means:
A. Replace RHS on stack with LHS
B. Push input
C. Accept input
D. Delete input
Correct Answer: A

Q111. Operator precedence parsing handles:
A. Operators with precedence/associativity, no consecutive non-terminals
B. All CFGs
C. Left recursion automatically
D. Semantic actions only
Correct Answer: A

Q112. Limitation of operator precedence:
A. Cannot handle epsilon / consecutive non-terminals well
B. Too powerful for all grammars
C. Needs LR table always
D. Cannot handle expressions
Correct Answer: A

Q113. LR parsing is:
A. Bottom-up, L=left-to-right scan, R=rightmost derivation reverse
B. Top-down
C. Left-recursive only
D. Lexical only
Correct Answer: A

Q114. LR(0) items have:
A. No lookahead
B. 1 lookahead
C. k lookaheads always >1
D. Infinite lookahead
Correct Answer: A

Q115. SLR uses:
A. FOLLOW sets for reduce decisions
B. FIRST only
C. No sets
D. Precedence only
Correct Answer: A

Q116. CLR(1)/LALR differ in:
A. Power and table size; LALR merges states
B. Both same power as SLR
C. Top-down vs bottom-up
D. Lex vs Yacc
Correct Answer: A

Q117. Most powerful among SLR, LALR, CLR:
A. Canonical LR
B. SLR
C. Operator precedence
D. Recursive descent
Correct Answer: A

Q118. YACC generates:
A. LALR parser (bottom-up)
B. Lexical analyzer
C. Top-down parser only
D. Code optimizer
Correct Answer: A

Q119. Input to YACC is:
A. CFG with actions/semantic routines
B. Regular expressions only
C. Object code
D. Quadruples
Correct Answer: A

Q120. YACC output is typically:
A. y.tab.c parser in C
B. lex.yy.c scanner
C. EXE
D. Symbol table only
Correct Answer: A

Q121. YACC works with Lex by:
A. Parser calls yylex() for tokens
B. Lex calls yyparse()
C. No interaction
D. Linker merges
Correct Answer: A

Q122. Conflict when both shift and reduce possible is:
A. Shift-reduce conflict
B. Reduce-reduce resolved automatically
C. Lex error
D. Link error
Correct Answer: A

Q123. Reduce-reduce conflict means:
A. Two reductions possible, needs grammar revision
B. Shift and reduce possible
C. No action
D. Accept
Correct Answer: A

Q124. Dangling else causes:
A. Shift-reduce conflict
B. Reduce-reduce conflict
C. Lex error
D. No conflict
Correct Answer: A

Q125. Viable prefix in LR parsing is:
A. Prefix of sentential form that can appear on stack
B. Any prefix of input
C. Suffix of grammar
D. Token prefix
Correct Answer: A

Q126. Augmented grammar adds:
A. New start S'->S
B. New terminal
C. Epsilon removal
D. Left factoring
Correct Answer: A

Q127. Top-down parsing builds parse tree from:
A. Root to leaves (start symbol)
B. Leaves to root
C. Middle out
D. Random
Correct Answer: A

Q128. Challenge for top-down:
A. Left recursion and backtracking
B. Shift-reduce conflicts
C. Relocation
D. Paging
Correct Answer: A

Q129. Left recursion example:
A. A->Aalph|beta
B. A->betaA|beta
C. A->aB
D. A->epsilon only
Correct Answer: A

Q130. Left recursion removal for A->Aalph|beta gives:
A. A->betaA', A'->alphA'|epsilon
B. A->alphaA|beta
C. A->beta only
D. A->Abeta
Correct Answer: A

Q131. Indirect left recursion is removed by:
A. Ordering and substitution algorithm
B. Direct substitution only one step
C. Left factoring
D. Precedence
Correct Answer: A

Q132. Recursive descent parsing is:
A. Top-down with recursive procedures for non-terminals
B. Bottom-up table driven
C. Operator precedence
D. LR
Correct Answer: A

Q133. Predictive parsing uses:
A. Lookahead to choose production without backtracking
B. Backtracking always
C. Stack of handles
D. Precedence table only
Correct Answer: A

Q134. LL(1) means:
A. Left-to-right, Leftmost derivation, 1 lookahead
B. Left-to-right, Left recursion, 1 pass
C. Leftmost rightmost 1 grammar
D. Lex lookahead 1
Correct Answer: A

Q135. FIRST(alpha) is set of:
A. Terminals beginning strings derived from alpha
B. Terminals following alpha
C. Non-terminals of alpha
D. Last symbols
Correct Answer: A

Q136. FOLLOW(A) is set of:
A. Terminals that can appear immediately after A
B. First of A
C. All productions of A
D. Start symbols
Correct Answer: A

Q137. LL(1) table M[A,a] uses:
A. FIRST and FOLLOW
B. LR items
C. Precedence
D. Symbol table
Correct Answer: A

Q138. Condition for LL(1) (no conflict):
A. Disjoint SELECT sets / FIRST-FOLLOW disjoint for epsilon-productions
B. Ambiguous grammar
C. Left recursive grammar
D. No FIRST needed
Correct Answer: A

Q139. Left factoring removes:
A. Common prefixes to enable predictive parsing
B. Left recursion
C. Ambiguity fully
D. Epsilon
Correct Answer: A

Q140. Example left factored: A->alpha beta1 | alpha beta2 becomes:
A. A->alpha A', A'->beta1|beta2
B. A->beta A'
C. A->alpha only
D. A->epsilon
Correct Answer: A

Q141. Backtracking in top-down is avoided by:
A. Predictive LL(1) tables
B. More backtracking
C. LR tables
D. Macros
Correct Answer: A

Q142. Which is top-down?
A. Recursive descent, LL, predictive
B. SLR, LALR, CLR
C. Operator precedence
D. Shift-reduce
Correct Answer: A

Q143. Which is bottom-up?
A. LR, SLR, LALR, operator precedence
B. LL, recursive descent
C. Predictive
D. Lex
Correct Answer: A

Q144. Semantic analysis checks:
A. Type consistency, declarations, scope
B. Token spelling
C. Whitespace
D. Address relocation
Correct Answer: A

Q145. Syntax-directed translation attaches:
A. Semantic actions/attributes to productions
B. Tokens to Lex only
C. Frames to pages
D. Macros to loader
Correct Answer: A

Q146. S-attributed definitions use:
A. Synthesized attributes only
B. Inherited only
C. Both unrestricted
D. No attributes
Correct Answer: A

Q147. L-attributed definitions allow:
A. Left-to-right evaluation (synthesized + inherited with restrictions)
B. Right-to-left only
C. No inherited
D. Random
Correct Answer: A

Q148. Three-address code has at most:
A. Three addresses (x=y op z)
B. One address
C. Five addresses
D. No addresses
Correct Answer: A

Q149. Quadruple fields are:
A. op, arg1, arg2, result
B. op, arg, result only
C. Three fields only
D. Two fields
Correct Answer: A

Q150. Triple fields are:
A. op, arg1, arg2 (result implicit by position)
B. op, arg1, arg2, result
C. Only op
D. Label only
Correct Answer: A

Q151. Indirect triples use:
A. Pointer list to triples
B. Direct result field
C. Quadruples
D. Symbol table only
Correct Answer: A

Q152. Advantage of triples over quadruples:
A. Saves space (no explicit temp names)
B. Faster code gen always
C. Easier optimization movement
D. No disadvantage
Correct Answer: A

Q153. Disadvantage of triples:
A. Moving code requires pointer updates / less flexible
B. Uses more space
C. Cannot represent expressions
D. Needs more temps
Correct Answer: A

Q154. Example a=b+c in quadruple:
A. (+,b,c,t1) then (=,t1,-,a)
B. (+,b,c)
C. (=,a,b)
D. (+,a,b,c,d,e)
Correct Answer: A

Q155. DAG for basic block helps in:
A. Detecting common subexpressions
B. Parsing
C. Lexing
D. Linking
Correct Answer: A

Q156. Basic block is:
A. Straight-line code with single entry/exit
B. Block with jumps inside
C. Function
D. Macro
Correct Answer: A

Q157. Flow graph nodes are:
A. Basic blocks
B. Tokens
C. Symbols
D. Frames
Correct Answer: A

Q158. Next-use information is used for:
A. Register allocation
B. Parsing
C. Lexing
D. Loading
Correct Answer: A

Q159. Peephole optimization examines:
A. Small window of instructions
B. Whole program
C. Grammar
D. Symbol table only
Correct Answer: A

Q160. Examples of peephole:
A. Redundant loads, strength reduction, dead code elimination locally
B. LR table compaction
C. Macro expansion
D. Deadlock avoidance
Correct Answer: A

Q161. Loop optimization includes:
A. Invariant hoisting, induction variable elimination, unrolling
B. Left factoring
C. Backpatching
D. Paging
Correct Answer: A

Q162. Common subexpression elimination is:
A. Global/local optimization avoiding recomputation
B. Parsing technique
C. Macro technique
D. Loading technique
Correct Answer: A

Q163. Copy propagation replaces:
A. Use of copy variable with original
B. Constants with variables
C. Loops with recursion
D. Tokens with lexemes
Correct Answer: A

Q164. Constant folding evaluates:
A. Constants at compile time
B. Variables at runtime
C. Grammar at parse time
D. Addresses at load time
Correct Answer: A

Q165. Strength reduction replaces:
A. Expensive ops with cheaper (e.g., *2 by shift)
B. Cheap with expensive
C. Loads with stores
D. Branches with calls
Correct Answer: A

Q166. Dead code elimination removes:
A. Unreachable / unused computation
B. Live code
C. Entry block
D. Symbol table
Correct Answer: A

Q167. Code motion moves:
A. Loop-invariant code out of loop
B. Code into loop
C. Tokens
D. Macros
Correct Answer: A

Q168. Register allocation aims to:
A. Minimize loads/stores, keep values in registers
B. Maximize memory access
C. Increase spills
D. Avoid registers
Correct Answer: A

Q169. Graph coloring is used for:
A. Register allocation
B. Parsing
C. Lexing
D. Scheduling
Correct Answer: A

Q170. Spilling occurs when:
A. Insufficient registers, value stored to memory
B. Sufficient registers
C. No interference
D. No variables
Correct Answer: A

Q171. Activation record contains:
A. Return address, locals, params, dynamic/static links
B. Only opcodes
C. Only tokens
D. Only macros
Correct Answer: A

Q172. Static link points to:
A. Enclosing scope activation for non-locals
B. Caller activation
C. Heap top
D. Code segment
Correct Answer: A

Q173. Dynamic link points to:
A. Caller activation record
B. Global data
C. Heap
D. Symbol table
Correct Answer: A

Q174. Parameter passing by value:
A. Copies actual to formal, callee changes not reflected
B. Reflects changes
C. Passes address
D. Passes name textually
Correct Answer: A

Q175. Call by reference passes:
A. Address, changes reflected
B. Copy only
C. Name string
D. Value only
Correct Answer: A

Q176. Display is used for:
A. Fast access to non-locals in nested scopes
B. Monitor display
C. Lex display
D. Loader display
Correct Answer: A

Q177. Heap allocation is needed for:
A. Dynamic data / recursion with variable lifetime
B. Static locals only
C. Compile-time constants only
D. Register allocation
Correct Answer: A

Q178. Duff's / Sethi-Ullman relates to:
A. Code generation / register number ordering
B. Parsing
C. Lexing
D. Linking
Correct Answer: A

Q179. Object code generation from IR must consider:
A. Target instruction selection, addressing modes
B. Grammar ambiguity only
C. Macro names only
D. Editor commands
Correct Answer: A

Q180. Cross-optimization concerns:
A. Machine-dependent vs independent levels
B. Only peephole
C. Only loops
D. Only macros
Correct Answer: A

Q181. Machine-independent optimization acts on:
A. Intermediate code
B. Target assembly only
C. Source text layout
D. Object layout on disk
Correct Answer: A

Q182. Machine-dependent optimization acts on:
A. Target code (registers, pipelines)
B. Tokens
C. Grammar
D. Symbol names
Correct Answer: A

Q183. Data-flow analysis includes:
A. Reaching definitions, live variables, available expressions
B. FIRST/FOLLOW only
C. Symbol table hashing only
D. Paging only
Correct Answer: A

Q184. Dominators in flow graphs are used for:
A. Finding loops / natural loops
B. Lexing
C. Macro expansion
D. Relocation
Correct Answer: A

Q185. Back edge (v->u where u dominates v) indicates:
A. Loop
B. Straight code
C. Dead code
D. Entry
Correct Answer: A

Q186. Which parsing is most general but slow?
A. CYK / Earley for general CFG
B. LL(1)
C. LR(1)
D. Operator precedence
Correct Answer: A

Q187. Handle pruning corresponds to:
A. Bottom-up parsing steps
B. Top-down expansion
C. Lex scanning
D. Optimization
Correct Answer: A

Q188. Kernel vs non-kernel LR items:
A. Kernel includes initial item and those with dot not at left except S'->.S
B. Same
C. Kernel is for LL
D. Non-kernel for Lex
Correct Answer: A

Q189. SLR table construction uses:
A. LR(0) automaton + FOLLOW
B. Canonical collection + lookaheads
C. Precedence matrix only
D. FIRST only
Correct Answer: A

Q190. LALR table size vs CLR:
A. Smaller (merged) but slightly less powerful
B. Larger
C. Same power always
D. Unrelated
Correct Answer: A

Q191. Error recovery in LR often uses:
A. Error productions / panic mode with synchronizing tokens
B. Ignoring all input
C. Reboot
D. Relocation
Correct Answer: A

Q192. Panic-mode recovery skips to:
A. Synchronizing token (e.g., ;, end)
B. Start of file always
C. End of program halt
D. Random token
Correct Answer: A

Q193. Phrase-level recovery:
A. Local correction (insert/delete) on error
B. Skip whole program
C. Reload OS
D. Reassemble
Correct Answer: A

Q194. Bootstrapping a compiler for new machine needs:
A. Cross-compiler then self-hosting
B. Only interpreter
C. Only loader
D. Only editor
Correct Answer: A

Q195. Self-compilation validates:
A. Compiler correctness via fixed point
B. Loader speed
C. Editor features
D. Macro power
Correct Answer: A

Q196. One-address machine uses:
A. Accumulator (e.g., ADD M)
B. Stack
C. Three registers
D. No addresses
Correct Answer: A

Q197. Zero-address machine uses:
A. Stack (PUSH/POP, ADD with no address)
B. Accumulator
C. Three addresses
D. Two addresses
Correct Answer: A

Q198. Assembly directive DB defines:
A. Byte(s) of data
B. Double word always 32-bit
C. Debugger breakpoint
D. Data bus
Correct Answer: A

Q199. DAD instruction in 8085:
A. Add HL with register pair (16-bit add)
B. Add 8-bit
C. Decimal adjust
D. Decrement
Correct Answer: A

Q200. DAA instruction is used for:
A. Decimal adjust after BCD addition
B. Data access
C. Direct addressing
D. Dynamic allocation
Correct Answer: A

---
## ANSWER KEY
1-A 2-B 3-A 4-A 5-B 6-B 7-B 8-A 9-A 10-A
11-A 12-A 13-A 14-A 15-A 16-A 17-A 18-A 19-A 20-A
21-A 22-A 23-A 24-B 25-A 26-A 27-A 28-A 29-A 30-A
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
181-A 182-A 183-A 184-A 185-A 186-A 187-A 188-A 189-A 190-A
191-A 192-A 193-A 194-A 195-A 196-A 197-A 198-A 199-A 200-A