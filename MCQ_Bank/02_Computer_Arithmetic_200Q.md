# Topic 2: Computer Arithmetic

**Syllabus:** Propositional (Boolean) Logic, Predicate Logic, Well-formed-formulae (WFF), Satisfiability and Tautology; Logic Families: TTL, ECL and C-MOS gates, Boolean algebra and Minimization of Boolean functions, Flip-flops - types, race condition and comparison, Design of combinational and sequential circuits; Representation of Integers: Octal, Hex, Decimal, and Binary, 2's complement and 1's complement arithmetic, Floating point representation.

Q1. Which of the following is a tautology?
A. p ∨ ¬p
B. p ∧ ¬p
C. p → ¬p
D. (p ∧ q) ∧ ¬q
Correct Answer: A

Q2. Which formula is unsatisfiable (contradiction)?
A. p ∨ ¬p
B. p → p
C. p ∧ ¬p
D. True
Correct Answer: C

Q3. A wff is satisfiable iff?
A. It is false in all interpretations
B. It is true in all interpretations
C. There exists an interpretation making it true
D. It has no models
Correct Answer: C

Q4. De Morgan's law states ¬(p ∨ q) equals?
A. p ∧ q
B. ¬p ∧ ¬q
C. ¬p ∨ ¬q
D. p ∨ q
Correct Answer: B

Q5. p → q is logically equivalent to?
A. ¬q ∨ p
B. p ∨ ¬q
C. ¬p ∨ q
D. p ∧ q
Correct Answer: C

Q6. Which logic family has the highest speed?
A. TTL
B. ECL
C. CMOS
D. RTL
Correct Answer: B

Q7. Which logic family has lowest static power dissipation?
A. CMOS
B. ECL
C. TTL
D. DTL
Correct Answer: A

Q8. TTL stands for?
A. Transistor-Transistor Logic
B. Time-Triggered Logic
C. Transistor-Timed Loop
D. Triode-Transistor Logic
Correct Answer: A

Q9. ECL's key characteristic is?
A. Saturated operation, low speed
B. Highest noise margin of all
C. Zero power
D. Non-saturated operation, very high speed but high power
Correct Answer: D

Q10. CMOS inverter in steady state draws?
A. Near-zero static current
B. Negative current
C. Large static current
D. Maximum current always
Correct Answer: A

Q11. Predicate ∀x P(x) is true when?
A. P holds for no x
B. P(x) holds for every x in domain
C. P holds for at least one x
D. P holds for finitely many x
Correct Answer: B

Q12. ∃x ∀y R(x,y) versus ∀y ∃x R(x,y): the former?
A. Is always false
B. Implies the latter but not conversely
C. Is weaker
D. Is equivalent
Correct Answer: B

Q13. Skolemization is used to?
A. Minimize gates
B. Convert to tautology
C. Eliminate universal quantifiers
D. Eliminate existential quantifiers preserving satisfiability
Correct Answer: D

Q14. A valid argument's conclusion must be true when?
A. At least one premise is true
B. Premises are false
C. Conclusion is satisfiable
D. All premises are true
Correct Answer: D

Q15. Resolution principle applies to formulas in?
A. Horn form only
B. Arithmetic form
C. Conjunctive normal form (clausal form)
D. Disjunctive normal form only
Correct Answer: C

Q16. Which of the following is logically equivalent to ¬(p ∧ q)?
A. p → q
B. p ∧ q
C. ¬p ∨ ¬q
D. ¬p ∧ ¬q
Correct Answer: C

Q17. The dual of Boolean expression A·(B+C) is?
A. A+B·C
B. A·B+C
C. A+(B·C)
D. (A+B)·C
Correct Answer: C

Q18. Fan-out of a logic gate refers to?
A. Power supply voltage
B. Number of outputs it has
C. Number of gate inputs it can drive
D. Propagation delay
Correct Answer: C

Q19. Noise margin is highest (among classic families) in?
A. CMOS
B. Schottky TTL
C. ECL
D. I2L
Correct Answer: A

Q20. A tautology with n variables is true in how many rows of truth table?
A. 4-1 rows
B. 2 rows
C. All 4 rows
D. Exactly 1 row
Correct Answer: C

Q21. Which of the following is logically equivalent to ¬(p ∧ q)?
A. ¬p ∨ ¬q
B. p ∧ q
C. ¬p ∧ ¬q
D. p → q
Correct Answer: A

Q22. The dual of Boolean expression A·(B+C) is?
A. (A+B)·C
B. A+(B·C)
C. A·B+C
D. A+B·C
Correct Answer: B

Q23. Fan-out of a logic gate refers to?
A. Number of gate inputs it can drive
B. Power supply voltage
C. Propagation delay
D. Number of outputs it has
Correct Answer: A

Q24. Noise margin is highest (among classic families) in?
A. ECL
B. Schottky TTL
C. CMOS
D. I2L
Correct Answer: C

Q25. A tautology with n variables is true in how many rows of truth table?
A. 16-1 rows
B. 4 rows
C. All 16 rows
D. Exactly 1 row
Correct Answer: C

Q26. Which of the following is logically equivalent to ¬(p ∧ q)?
A. ¬p ∨ ¬q
B. ¬p ∧ ¬q
C. p ∧ q
D. p → q
Correct Answer: A

Q27. The dual of Boolean expression A·(B+C) is?
A. A+B·C
B. (A+B)·C
C. A·B+C
D. A+(B·C)
Correct Answer: D

Q28. Fan-out of a logic gate refers to?
A. Number of gate inputs it can drive
B. Number of outputs it has
C. Power supply voltage
D. Propagation delay
Correct Answer: A

Q29. Noise margin is highest (among classic families) in?
A. ECL
B. CMOS
C. Schottky TTL
D. I2L
Correct Answer: B

Q30. A tautology with n variables is true in how many rows of truth table?
A. All 16 rows
B. 4 rows
C. Exactly 1 row
D. 16-1 rows
Correct Answer: A

Q31. Which of the following is logically equivalent to ¬(p ∧ q)?
A. p ∧ q
B. ¬p ∨ ¬q
C. p → q
D. ¬p ∧ ¬q
Correct Answer: B

Q32. The dual of Boolean expression A·(B+C) is?
A. A+B·C
B. A·B+C
C. (A+B)·C
D. A+(B·C)
Correct Answer: D

Q33. Fan-out of a logic gate refers to?
A. Propagation delay
B. Number of gate inputs it can drive
C. Number of outputs it has
D. Power supply voltage
Correct Answer: B

Q34. Noise margin is highest (among classic families) in?
A. I2L
B. Schottky TTL
C. ECL
D. CMOS
Correct Answer: D

Q35. A tautology with n variables is true in how many rows of truth table?
A. 2 rows
B. All 4 rows
C. Exactly 1 row
D. 4-1 rows
Correct Answer: B

Q36. Which of the following is logically equivalent to ¬(p ∧ q)?
A. ¬p ∧ ¬q
B. p → q
C. p ∧ q
D. ¬p ∨ ¬q
Correct Answer: D

Q37. The dual of Boolean expression A·(B+C) is?
A. A+B·C
B. A+(B·C)
C. A·B+C
D. (A+B)·C
Correct Answer: B

Q38. Fan-out of a logic gate refers to?
A. Number of outputs it has
B. Power supply voltage
C. Number of gate inputs it can drive
D. Propagation delay
Correct Answer: C

Q39. Noise margin is highest (among classic families) in?
A. CMOS
B. I2L
C. Schottky TTL
D. ECL
Correct Answer: A

Q40. A tautology with n variables is true in how many rows of truth table?
A. All 4 rows
B. 2 rows
C. 4-1 rows
D. Exactly 1 row
Correct Answer: A

Q41. Which of the following is logically equivalent to ¬(p ∧ q)?
A. p → q
B. ¬p ∨ ¬q
C. p ∧ q
D. ¬p ∧ ¬q
Correct Answer: B

Q42. The dual of Boolean expression A·(B+C) is?
A. A·B+C
B. A+(B·C)
C. A+B·C
D. (A+B)·C
Correct Answer: B

Q43. Fan-out of a logic gate refers to?
A. Propagation delay
B. Number of outputs it has
C. Power supply voltage
D. Number of gate inputs it can drive
Correct Answer: D

Q44. Noise margin is highest (among classic families) in?
A. ECL
B. CMOS
C. I2L
D. Schottky TTL
Correct Answer: B

Q45. A tautology with n variables is true in how many rows of truth table?
A. 2 rows
B. Exactly 1 row
C. All 4 rows
D. 4-1 rows
Correct Answer: C

Q46. Which of the following is logically equivalent to ¬(p ∧ q)?
A. p ∧ q
B. ¬p ∧ ¬q
C. ¬p ∨ ¬q
D. p → q
Correct Answer: C

Q47. The dual of Boolean expression A·(B+C) is?
A. A+(B·C)
B. A+B·C
C. A·B+C
D. (A+B)·C
Correct Answer: A

Q48. Fan-out of a logic gate refers to?
A. Power supply voltage
B. Number of gate inputs it can drive
C. Number of outputs it has
D. Propagation delay
Correct Answer: B

Q49. Noise margin is highest (among classic families) in?
A. Schottky TTL
B. I2L
C. CMOS
D. ECL
Correct Answer: C

Q50. A tautology with n variables is true in how many rows of truth table?
A. All 16 rows
B. Exactly 1 row
C. 16-1 rows
D. 4 rows
Correct Answer: A

Q51. An n-variable K-map (n=4) has how many cells?
A. 8
B. 17
C. 16
D. 16
Correct Answer: C

Q52. In a K-map, groups must contain cells in powers of?
A. 2 (1,2,4,8,...)
B. 3
C. 10
D. 5
Correct Answer: A

Q53. Quine-McCluskey method is used for?
A. Floating-point rounding
B. Encoding flip-flops
C. Designing ALUs
D. Tabular minimization of Boolean functions, finding prime implicants
Correct Answer: D

Q54. An essential prime implicant is one that?
A. Covers a minterm covered by no other prime implicant
B. Is always redundant
C. Has the largest cost
D. Covers all minterms
Correct Answer: A

Q55. A 4:1 multiplexer has how many select lines?
A. 4
B. 5
C. 2
D. 3
Correct Answer: C

Q56. A 4-to-16 decoder has how many output lines?
A. 16
B. 8
C. 5
D. 4
Correct Answer: A

Q57. Race-around condition occurs in?
A. D flip-flop always
B. ROM
C. JK flip-flop with J=K=1 and long clock pulse
D. Combinational gates only
Correct Answer: C

Q58. Master-slave JK flip-flop was introduced to overcome?
A. Fan-in limit
B. Power dissipation
C. Race-around condition
D. Clock skew only
Correct Answer: C

Q59. Characteristic equation of D flip-flop (next state Q+) is?
A. Q+ = JQ'+K'Q
B. Q+ = D
C. Q+ = Q'
D. Q+ = T xor Q
Correct Answer: B

Q60. Characteristic equation of JK flip-flop is?
A. Q+ = TQ'+T'Q
B. Q+ = JQ' + K'Q
C. Q+ = SQ+R'Q
D. Q+ = D
Correct Answer: B

Q61. A mod-8 ripple counter requires at least how many flip-flops?
A. 8
B. 7
C. 3
D. 4
Correct Answer: C

Q62. A combinational circuit's output depends on?
A. Present inputs only
B. Previous output only
C. Present + past inputs
D. Clock only
Correct Answer: A

Q63. A sequential circuit's output depends on?
A. Temperature only
B. Power supply only
C. Present inputs and present state (past inputs)
D. Present inputs only
Correct Answer: C

Q64. Gray code of binary 1011 is? (adjacent codes differ by 1 bit)
A. 1010
B. 1101
C. 1110
D. 0100
Correct Answer: C

Q65. The Boolean function F=A+A'B equals (absorption)?
A. A
B. A'B'
C. A'B
D. A+B
Correct Answer: D

Q66. Minimum number of NAND gates to implement NOT, AND, OR respectively (using NAND only)?
A. 1,1,1
B. 3,2,1
C. 1, 2, 3
D. 2,2,2
Correct Answer: C

Q67. A half-adder has inputs/outputs?
A. 2 inputs, 1 output
B. 3 inputs, 2 outputs
C. 2 inputs, 2 outputs (Sum, Carry)
D. 1 input, 2 outputs
Correct Answer: C

Q68. A full-adder can be built from how many half-adders + OR?
A. 1 half-adder
B. 2 half-adders + 1 OR gate
C. 4 half-adders
D. 3 half-adders
Correct Answer: B

Q69. Propagation delay in ripple-carry adder grows as?
A. O(n) with number of bits
B. O(n^2)
C. O(1)
D. O(log n) always
Correct Answer: A

Q70. Edge-triggered flip-flop samples input on?
A. Entire HIGH level
B. Both levels continuously
C. Active clock edge only
D. Entire LOW level
Correct Answer: C

Q71. An n-variable K-map (n=3) has how many cells?
A. 8
B. 6
C. 9
D. 9
Correct Answer: A

Q72. In a K-map, groups must contain cells in powers of?
A. 3
B. 2 (1,2,4,8,...)
C. 5
D. 10
Correct Answer: B

Q73. Quine-McCluskey method is used for?
A. Encoding flip-flops
B. Floating-point rounding
C. Tabular minimization of Boolean functions, finding prime implicants
D. Designing ALUs
Correct Answer: C

Q74. An essential prime implicant is one that?
A. Covers all minterms
B. Covers a minterm covered by no other prime implicant
C. Is always redundant
D. Has the largest cost
Correct Answer: B

Q75. A 2:1 multiplexer has how many select lines?
A. 2
B. 3
C. 2
D. 1
Correct Answer: D

Q76. A 4-to-16 decoder has how many output lines?
A. 5
B. 8
C. 16
D. 4
Correct Answer: C

Q77. Race-around condition occurs in?
A. ROM
B. JK flip-flop with J=K=1 and long clock pulse
C. D flip-flop always
D. Combinational gates only
Correct Answer: B

Q78. Master-slave JK flip-flop was introduced to overcome?
A. Race-around condition
B. Clock skew only
C. Power dissipation
D. Fan-in limit
Correct Answer: A

Q79. Characteristic equation of D flip-flop (next state Q+) is?
A. Q+ = D
B. Q+ = T xor Q
C. Q+ = Q'
D. Q+ = JQ'+K'Q
Correct Answer: A

Q80. Characteristic equation of JK flip-flop is?
A. Q+ = JQ' + K'Q
B. Q+ = SQ+R'Q
C. Q+ = D
D. Q+ = TQ'+T'Q
Correct Answer: A

Q81. A mod-10 ripple counter requires at least how many flip-flops?
A. 5
B. 9
C. 4
D. 10
Correct Answer: C

Q82. A combinational circuit's output depends on?
A. Present + past inputs
B. Previous output only
C. Present inputs only
D. Clock only
Correct Answer: C

Q83. A sequential circuit's output depends on?
A. Temperature only
B. Present inputs and present state (past inputs)
C. Power supply only
D. Present inputs only
Correct Answer: B

Q84. Gray code of binary 1011 is? (adjacent codes differ by 1 bit)
A. 1110
B. 1101
C. 0100
D. 1010
Correct Answer: A

Q85. The Boolean function F=A+A'B equals (absorption)?
A. A'B
B. A'B'
C. A+B
D. A
Correct Answer: C

Q86. Minimum number of NAND gates to implement NOT, AND, OR respectively (using NAND only)?
A. 2,2,2
B. 1,1,1
C. 3,2,1
D. 1, 2, 3
Correct Answer: D

Q87. A half-adder has inputs/outputs?
A. 2 inputs, 1 output
B. 3 inputs, 2 outputs
C. 1 input, 2 outputs
D. 2 inputs, 2 outputs (Sum, Carry)
Correct Answer: D

Q88. A full-adder can be built from how many half-adders + OR?
A. 2 half-adders + 1 OR gate
B. 3 half-adders
C. 1 half-adder
D. 4 half-adders
Correct Answer: A

Q89. Propagation delay in ripple-carry adder grows as?
A. O(log n) always
B. O(n) with number of bits
C. O(n^2)
D. O(1)
Correct Answer: B

Q90. Edge-triggered flip-flop samples input on?
A. Entire HIGH level
B. Active clock edge only
C. Both levels continuously
D. Entire LOW level
Correct Answer: B

Q91. An n-variable K-map (n=2) has how many cells?
A. 4
B. 4
C. 5
D. 4
Correct Answer: A

Q92. In a K-map, groups must contain cells in powers of?
A. 2 (1,2,4,8,...)
B. 10
C. 5
D. 3
Correct Answer: A

Q93. Quine-McCluskey method is used for?
A. Designing ALUs
B. Floating-point rounding
C. Tabular minimization of Boolean functions, finding prime implicants
D. Encoding flip-flops
Correct Answer: C

Q94. An essential prime implicant is one that?
A. Covers all minterms
B. Is always redundant
C. Covers a minterm covered by no other prime implicant
D. Has the largest cost
Correct Answer: C

Q95. A 2:1 multiplexer has how many select lines?
A. 2
B. 3
C. 2
D. 1
Correct Answer: D

Q96. A 3-to-8 decoder has how many output lines?
A. 8
B. 3
C. 6
D. 4
Correct Answer: A

Q97. Race-around condition occurs in?
A. JK flip-flop with J=K=1 and long clock pulse
B. ROM
C. D flip-flop always
D. Combinational gates only
Correct Answer: A

Q98. Master-slave JK flip-flop was introduced to overcome?
A. Clock skew only
B. Power dissipation
C. Race-around condition
D. Fan-in limit
Correct Answer: C

Q99. Characteristic equation of D flip-flop (next state Q+) is?
A. Q+ = Q'
B. Q+ = D
C. Q+ = JQ'+K'Q
D. Q+ = T xor Q
Correct Answer: B

Q100. Characteristic equation of JK flip-flop is?
A. Q+ = SQ+R'Q
B. Q+ = JQ' + K'Q
C. Q+ = D
D. Q+ = TQ'+T'Q
Correct Answer: B

Q101. A mod-16 ripple counter requires at least how many flip-flops?
A. 5
B. 16
C. 15
D. 4
Correct Answer: D

Q102. A combinational circuit's output depends on?
A. Clock only
B. Present inputs only
C. Present + past inputs
D. Previous output only
Correct Answer: B

Q103. A sequential circuit's output depends on?
A. Power supply only
B. Temperature only
C. Present inputs and present state (past inputs)
D. Present inputs only
Correct Answer: C

Q104. Gray code of binary 1011 is? (adjacent codes differ by 1 bit)
A. 0100
B. 1010
C. 1110
D. 1101
Correct Answer: C

Q105. The Boolean function F=A+A'B equals (absorption)?
A. A'B
B. A
C. A'B'
D. A+B
Correct Answer: D

Q106. Minimum number of NAND gates to implement NOT, AND, OR respectively (using NAND only)?
A. 3,2,1
B. 1, 2, 3
C. 1,1,1
D. 2,2,2
Correct Answer: B

Q107. A half-adder has inputs/outputs?
A. 3 inputs, 2 outputs
B. 1 input, 2 outputs
C. 2 inputs, 2 outputs (Sum, Carry)
D. 2 inputs, 1 output
Correct Answer: C

Q108. A full-adder can be built from how many half-adders + OR?
A. 4 half-adders
B. 2 half-adders + 1 OR gate
C. 3 half-adders
D. 1 half-adder
Correct Answer: B

Q109. Propagation delay in ripple-carry adder grows as?
A. O(log n) always
B. O(n^2)
C. O(1)
D. O(n) with number of bits
Correct Answer: D

Q110. Edge-triggered flip-flop samples input on?
A. Entire LOW level
B. Entire HIGH level
C. Both levels continuously
D. Active clock edge only
Correct Answer: D

Q111. An n-variable K-map (n=4) has how many cells?
A. 16
B. 16
C. 8
D. 17
Correct Answer: A

Q112. In a K-map, groups must contain cells in powers of?
A. 3
B. 2 (1,2,4,8,...)
C. 5
D. 10
Correct Answer: B

Q113. Quine-McCluskey method is used for?
A. Floating-point rounding
B. Designing ALUs
C. Encoding flip-flops
D. Tabular minimization of Boolean functions, finding prime implicants
Correct Answer: D

Q114. An essential prime implicant is one that?
A. Is always redundant
B. Covers all minterms
C. Has the largest cost
D. Covers a minterm covered by no other prime implicant
Correct Answer: D

Q115. A 2:1 multiplexer has how many select lines?
A. 2
B. 3
C. 1
D. 2
Correct Answer: C

Q116. A 4-to-16 decoder has how many output lines?
A. 8
B. 5
C. 16
D. 4
Correct Answer: C

Q117. Race-around condition occurs in?
A. D flip-flop always
B. Combinational gates only
C. JK flip-flop with J=K=1 and long clock pulse
D. ROM
Correct Answer: C

Q118. Master-slave JK flip-flop was introduced to overcome?
A. Power dissipation
B. Race-around condition
C. Clock skew only
D. Fan-in limit
Correct Answer: B

Q119. Characteristic equation of D flip-flop (next state Q+) is?
A. Q+ = Q'
B. Q+ = D
C. Q+ = JQ'+K'Q
D. Q+ = T xor Q
Correct Answer: B

Q120. Characteristic equation of JK flip-flop is?
A. Q+ = D
B. Q+ = JQ' + K'Q
C. Q+ = SQ+R'Q
D. Q+ = TQ'+T'Q
Correct Answer: B

Q121. A mod-8 ripple counter requires at least how many flip-flops?
A. 8
B. 3
C. 4
D. 7
Correct Answer: B

Q122. A combinational circuit's output depends on?
A. Present inputs only
B. Previous output only
C. Clock only
D. Present + past inputs
Correct Answer: A

Q123. A sequential circuit's output depends on?
A. Present inputs only
B. Power supply only
C. Present inputs and present state (past inputs)
D. Temperature only
Correct Answer: C

Q124. Gray code of binary 1011 is? (adjacent codes differ by 1 bit)
A. 1010
B. 1110
C. 0100
D. 1101
Correct Answer: B

Q125. The Boolean function F=A+A'B equals (absorption)?
A. A
B. A'B'
C. A'B
D. A+B
Correct Answer: D

Q126. Minimum number of NAND gates to implement NOT, AND, OR respectively (using NAND only)?
A. 2,2,2
B. 1,1,1
C. 1, 2, 3
D. 3,2,1
Correct Answer: C

Q127. A half-adder has inputs/outputs?
A. 3 inputs, 2 outputs
B. 2 inputs, 2 outputs (Sum, Carry)
C. 1 input, 2 outputs
D. 2 inputs, 1 output
Correct Answer: B

Q128. A full-adder can be built from how many half-adders + OR?
A. 3 half-adders
B. 4 half-adders
C. 1 half-adder
D. 2 half-adders + 1 OR gate
Correct Answer: D

Q129. Propagation delay in ripple-carry adder grows as?
A. O(log n) always
B. O(1)
C. O(n^2)
D. O(n) with number of bits
Correct Answer: D

Q130. Edge-triggered flip-flop samples input on?
A. Active clock edge only
B. Entire LOW level
C. Both levels continuously
D. Entire HIGH level
Correct Answer: A

Q131. An n-variable K-map (n=3) has how many cells?
A. 8
B. 9
C. 9
D. 6
Correct Answer: A

Q132. In a K-map, groups must contain cells in powers of?
A. 3
B. 2 (1,2,4,8,...)
C. 5
D. 10
Correct Answer: B

Q133. Quine-McCluskey method is used for?
A. Designing ALUs
B. Encoding flip-flops
C. Tabular minimization of Boolean functions, finding prime implicants
D. Floating-point rounding
Correct Answer: C

Q134. An essential prime implicant is one that?
A. Is always redundant
B. Covers all minterms
C. Has the largest cost
D. Covers a minterm covered by no other prime implicant
Correct Answer: D

Q135. A 2:1 multiplexer has how many select lines?
A. 1
B. 2
C. 2
D. 3
Correct Answer: A

Q136. A 3-to-8 decoder has how many output lines?
A. 8
B. 3
C. 4
D. 6
Correct Answer: A

Q137. Race-around condition occurs in?
A. JK flip-flop with J=K=1 and long clock pulse
B. ROM
C. Combinational gates only
D. D flip-flop always
Correct Answer: A

Q138. Master-slave JK flip-flop was introduced to overcome?
A. Fan-in limit
B. Power dissipation
C. Clock skew only
D. Race-around condition
Correct Answer: D

Q139. Characteristic equation of D flip-flop (next state Q+) is?
A. Q+ = JQ'+K'Q
B. Q+ = D
C. Q+ = T xor Q
D. Q+ = Q'
Correct Answer: B

Q140. Characteristic equation of JK flip-flop is?
A. Q+ = SQ+R'Q
B. Q+ = TQ'+T'Q
C. Q+ = D
D. Q+ = JQ' + K'Q
Correct Answer: D

Q141. A mod-8 ripple counter requires at least how many flip-flops?
A. 8
B. 7
C. 4
D. 3
Correct Answer: D

Q142. A combinational circuit's output depends on?
A. Previous output only
B. Present inputs only
C. Present + past inputs
D. Clock only
Correct Answer: B

Q143. A sequential circuit's output depends on?
A. Present inputs only
B. Power supply only
C. Present inputs and present state (past inputs)
D. Temperature only
Correct Answer: C

Q144. Gray code of binary 1011 is? (adjacent codes differ by 1 bit)
A. 1110
B. 0100
C. 1101
D. 1010
Correct Answer: A

Q145. The Boolean function F=A+A'B equals (absorption)?
A. A
B. A+B
C. A'B'
D. A'B
Correct Answer: B

Q146. Minimum number of NAND gates to implement NOT, AND, OR respectively (using NAND only)?
A. 2,2,2
B. 1, 2, 3
C. 1,1,1
D. 3,2,1
Correct Answer: B

Q147. A half-adder has inputs/outputs?
A. 2 inputs, 2 outputs (Sum, Carry)
B. 2 inputs, 1 output
C. 3 inputs, 2 outputs
D. 1 input, 2 outputs
Correct Answer: A

Q148. A full-adder can be built from how many half-adders + OR?
A. 4 half-adders
B. 2 half-adders + 1 OR gate
C. 3 half-adders
D. 1 half-adder
Correct Answer: B

Q149. Propagation delay in ripple-carry adder grows as?
A. O(n) with number of bits
B. O(n^2)
C. O(1)
D. O(log n) always
Correct Answer: A

Q150. Edge-triggered flip-flop samples input on?
A. Both levels continuously
B. Entire HIGH level
C. Entire LOW level
D. Active clock edge only
Correct Answer: D

Q151. Decimal 109 in 8-bit binary is?
A. 1101101
B. 01101110
C. 01101101
D. 01101100
Correct Answer: C

Q152. Decimal 222 in hexadecimal (2 digits) is?
A. 0xDF
B. 0o336
C. 0xDD
D. 0xDE
Correct Answer: D

Q153. Decimal 86 in octal is?
A. 127
B. 126
C. 125
D. 56
Correct Answer: B

Q154. Range of signed integers in 3-bit 2's complement is?
A. -4 to +3
B. 0 to 7
C. -7 to 7
D. 0 to 8
Correct Answer: A

Q155. 1's complement of binary 01101 is?
A. 01101
B. 10010
C. 00000
D. 11111
Correct Answer: B

Q156. In IEEE 754 single precision, exponent bias is?
A. 1023
B. 128
C. 127
D. 15
Correct Answer: C

Q157. In IEEE 754 single precision (32-bit), bit-fields are?
A. 1+7+24
B. 1+11+20
C. 8+8+16
D. 1 sign + 8 exponent + 23 mantissa
Correct Answer: D

Q158. In IEEE 754 double precision, exponent bias is?
A. 1023
B. 127
C. 63
D. 2047
Correct Answer: A

Q159. Binary 1100 + 0111 equals decimal?
A. 18
B. 19
C. 84
D. 20
Correct Answer: B

Q160. Overflow in 2's complement addition occurs when?
A. There is any carry
B. Operands have opposite signs
C. Carry into sign bit differs from carry out
D. Result is zero
Correct Answer: C

Q161. Decimal 103 in 8-bit binary is?
A. 01100111
B. 01100110
C. 1100111
D. 01101000
Correct Answer: A

Q162. Decimal 55 in hexadecimal (2 digits) is?
A. 0x38
B. 0o067
C. 0x36
D. 0x37
Correct Answer: D

Q163. Decimal 87 in octal is?
A. 126
B. 130
C. 127
D. 57
Correct Answer: C

Q164. Range of signed integers in 5-bit 2's complement is?
A. -31 to 31
B. -16 to +15
C. 0 to 32
D. 0 to 31
Correct Answer: B

Q165. 1's complement of binary 10110 is?
A. 01001
B. 10110
C. 11111
D. 00000
Correct Answer: A

Q166. In IEEE 754 single precision, exponent bias is?
A. 128
B. 15
C. 127
D. 1023
Correct Answer: C

Q167. In IEEE 754 single precision (32-bit), bit-fields are?
A. 1 sign + 8 exponent + 23 mantissa
B. 8+8+16
C. 1+7+24
D. 1+11+20
Correct Answer: A

Q168. In IEEE 754 double precision, exponent bias is?
A. 1023
B. 63
C. 2047
D. 127
Correct Answer: A

Q169. Binary 1110 + 0010 equals decimal?
A. 17
B. 16
C. 28
D. 15
Correct Answer: B

Q170. Overflow in 2's complement addition occurs when?
A. Result is zero
B. There is any carry
C. Operands have opposite signs
D. Carry into sign bit differs from carry out
Correct Answer: D

Q171. Decimal 14 in 8-bit binary is?
A. 0001110
B. 00001110
C. 00001111
D. 00001101
Correct Answer: B

Q172. Decimal 194 in hexadecimal (2 digits) is?
A. 0xC2
B. 0xC3
C. 0xC1
D. 0o302
Correct Answer: A

Q173. Decimal 80 in octal is?
A. 117
B. 121
C. 50
D. 120
Correct Answer: D

Q174. Range of signed integers in 7-bit 2's complement is?
A. 0 to 127
B. -64 to +63
C. 0 to 128
D. -127 to 127
Correct Answer: B

Q175. 1's complement of binary 10011 is?
A. 11111
B. 01100
C. 10011
D. 00000
Correct Answer: B

Q176. In IEEE 754 single precision, exponent bias is?
A. 127
B. 128
C. 15
D. 1023
Correct Answer: A

Q177. In IEEE 754 single precision (32-bit), bit-fields are?
A. 1 sign + 8 exponent + 23 mantissa
B. 1+7+24
C. 8+8+16
D. 1+11+20
Correct Answer: A

Q178. In IEEE 754 double precision, exponent bias is?
A. 63
B. 1023
C. 2047
D. 127
Correct Answer: B

Q179. Binary 0010 + 0011 equals decimal?
A. 6
B. 6
C. 4
D. 5
Correct Answer: D

Q180. Overflow in 2's complement addition occurs when?
A. Operands have opposite signs
B. There is any carry
C. Result is zero
D. Carry into sign bit differs from carry out
Correct Answer: D

Q181. Decimal 79 in 8-bit binary is?
A. 01001111
B. 1001111
C. 01001110
D. 01010000
Correct Answer: A

Q182. Decimal 73 in hexadecimal (2 digits) is?
A. 0x4A
B. 0x48
C. 0x49
D. 0o111
Correct Answer: C

Q183. Decimal 38 in octal is?
A. 26
B. 46
C. 45
D. 47
Correct Answer: B

Q184. Range of signed integers in 6-bit 2's complement is?
A. -32 to +31
B. 0 to 64
C. -63 to 63
D. 0 to 63
Correct Answer: A

Q185. 1's complement of binary 01101 is?
A. 00000
B. 11111
C. 01101
D. 10010
Correct Answer: D

Q186. In IEEE 754 single precision, exponent bias is?
A. 1023
B. 15
C. 127
D. 128
Correct Answer: C

Q187. In IEEE 754 single precision (32-bit), bit-fields are?
A. 1+7+24
B. 8+8+16
C. 1 sign + 8 exponent + 23 mantissa
D. 1+11+20
Correct Answer: C

Q188. In IEEE 754 double precision, exponent bias is?
A. 127
B. 63
C. 2047
D. 1023
Correct Answer: D

Q189. Binary 0011 + 0111 equals decimal?
A. 21
B. 11
C. 9
D. 10
Correct Answer: D

Q190. Overflow in 2's complement addition occurs when?
A. Result is zero
B. Carry into sign bit differs from carry out
C. There is any carry
D. Operands have opposite signs
Correct Answer: B

Q191. Decimal 145 in 8-bit binary is?
A. 10010001
B. 10010000
C. 10010001
D. 10010010
Correct Answer: A

Q192. Decimal 25 in hexadecimal (2 digits) is?
A. 0x19
B. 0x18
C. 0x1A
D. 0o031
Correct Answer: A

Q193. Decimal 18 in octal is?
A. 23
B. 21
C. 12
D. 22
Correct Answer: D

Q194. Range of signed integers in 7-bit 2's complement is?
A. 0 to 128
B. -64 to +63
C. 0 to 127
D. -127 to 127
Correct Answer: B

Q195. 1's complement of binary 11001 is?
A. 11111
B. 00000
C. 11001
D. 00110
Correct Answer: D

Q196. In IEEE 754 single precision, exponent bias is?
A. 1023
B. 15
C. 128
D. 127
Correct Answer: D

Q197. In IEEE 754 single precision (32-bit), bit-fields are?
A. 1+11+20
B. 1+7+24
C. 8+8+16
D. 1 sign + 8 exponent + 23 mantissa
Correct Answer: D

Q198. In IEEE 754 double precision, exponent bias is?
A. 2047
B. 63
C. 1023
D. 127
Correct Answer: C

Q199. Binary 0110 + 0110 equals decimal?
A. 12
B. 11
C. 13
D. 36
Correct Answer: A

Q200. Overflow in 2's complement addition occurs when?
A. Carry into sign bit differs from carry out
B. Operands have opposite signs
C. There is any carry
D. Result is zero
Correct Answer: A

---
## ANSWER KEY
1-A 2-C 3-C 4-B 5-C 6-B 7-A 8-A 9-D 10-A
11-B 12-B 13-D 14-D 15-C 16-C 17-C 18-C 19-A 20-C
21-A 22-B 23-A 24-C 25-C 26-A 27-D 28-A 29-B 30-A
31-B 32-D 33-B 34-D 35-B 36-D 37-B 38-C 39-A 40-A
41-B 42-B 43-D 44-B 45-C 46-C 47-A 48-B 49-C 50-A
51-C 52-A 53-D 54-A 55-C 56-A 57-C 58-C 59-B 60-B
61-C 62-A 63-C 64-C 65-D 66-C 67-C 68-B 69-A 70-C
71-A 72-B 73-C 74-B 75-D 76-C 77-B 78-A 79-A 80-A
81-C 82-C 83-B 84-A 85-C 86-D 87-D 88-A 89-B 90-B
91-A 92-A 93-C 94-C 95-D 96-A 97-A 98-C 99-B 100-B
101-D 102-B 103-C 104-C 105-D 106-B 107-C 108-B 109-D 110-D
111-A 112-B 113-D 114-D 115-C 116-C 117-C 118-B 119-B 120-B
121-B 122-A 123-C 124-B 125-D 126-C 127-B 128-D 129-D 130-A
131-A 132-B 133-C 134-D 135-A 136-A 137-A 138-D 139-B 140-D
141-D 142-B 143-C 144-A 145-B 146-B 147-A 148-B 149-A 150-D
151-C 152-D 153-B 154-A 155-B 156-C 157-D 158-A 159-B 160-C
161-A 162-D 163-C 164-B 165-A 166-C 167-A 168-A 169-B 170-D
171-B 172-A 173-D 174-B 175-B 176-A 177-A 178-B 179-D 180-D
181-A 182-C 183-B 184-A 185-D 186-C 187-C 188-D 189-D 190-B
191-A 192-A 193-D 194-B 195-D 196-D 197-D 198-C 199-A 200-A
