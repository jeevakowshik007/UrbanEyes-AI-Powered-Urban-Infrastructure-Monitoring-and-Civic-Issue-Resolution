# Topic 12c: Data Warehousing and Mining

**Syllabus:** Data Warehousing: Data Warehouse environment, architecture of a data warehouse methodology, analysis, design, construction and administration; Data Mining: Extracting models and patterns from large databases, data mining techniques, classification, regression, clustering, summarization, dependency modeling, link analysis, sequencing analysis, mining scientific and business data.

Q1. Data warehouse is?
A. Subject-oriented integrated time-variant nonvolatile
B. Transactional only
C. Temporary cache
D. Operational file
Correct Answer: A

Q2. Data warehouse environment includes?
A. Source/staging/warehouse/marts
B. Printer only
C. Keyboard only
D. CPU only
Correct Answer: A

Q3. OLTP focuses on?
A. Day-to-day transactions
B. Analysis only
C. Mining only
D. Archiving only
Correct Answer: A

Q4. OLAP focuses on?
A. Analysis/decision support
B. Transactions only
C. Data entry only
D. Billing only
Correct Answer: A

Q5. OLTP vs OLAP: data in OLTP is?
A. Current detailed normalized
B. Historical multidimensional
C. Aggregated only
D. External only
Correct Answer: A

Q6. OLAP query type is?
A. Complex ad-hoc multidimensional
B. Simple short update
C. Delete only
D. Insert only
Correct Answer: A

Q7. Warehouse architecture tiers commonly?
A. 3-tier
B. 1-tier only
C. No tier
D. 10-tier
Correct Answer: A

Q8. Bottom tier is?
A. Warehouse server/RDBMS
B. Client browser
C. Printer
D. OLAP server
Correct Answer: A

Q9. Middle tier is?
A. OLAP server
B. Data source
C. Monitor
D. Keyboard
Correct Answer: A

Q10. Top tier is?
A. Client/query tools
B. Disk only
C. Tape only
D. Source DB
Correct Answer: A

Q11. Data warehouse methodology steps include?
A. Analysis/design/construction/admin
B. Coding only
C. Testing only
D. Purchase only
Correct Answer: A

Q12. Requirement analysis in warehouse collects?
A. Business needs/KPIs
B. Hardware color
C. Staff age
D. Office size
Correct Answer: A

Q13. Dimensional modeling designs?
A. Facts/dimensions
B. ER only
C. Network only
D. Files only
Correct Answer: A

Q14. Fact table contains?
A. Measures/metrics
B. Only text
C. Only keys
D. Only names
Correct Answer: A

Q15. Dimension table contains?
A. Descriptive attributes
B. Only measures
C. Only facts
D. No data
Correct Answer: A

Q16. Star schema has?
A. Central fact + denormalized dims
B. Fully normalized
C. No fact
D. No dims
Correct Answer: A

Q17. Snowflake schema is?
A. Normalized dimensions
B. Denormalized only
C. No fact
D. Star with no center
Correct Answer: A

Q18. Star vs snowflake: query speed?
A. Star faster (fewer joins)
B. Snowflake always faster
C. Equal always
D. No queries
Correct Answer: A

Q19. Fact constellation is?
A. Multiple facts sharing dims
B. Single fact only
C. No facts
D. Only dims
Correct Answer: A

Q20. Slowly changing dimension Type 2?
A. New row per change
B. Overwrite
C. No history
D. Delete
Correct Answer: A

Q21. ETL stands for?
A. Extract Transform Load
B. Enter Table Load
C. Extract Table Link
D. Event Time Log
Correct Answer: A

Q22. Staging area is for?
A. Cleaning/transform before load
B. User queries
C. Final reports
D. Archiving only
Correct Answer: A

Q23. Data cleaning handles?
A. Missing/noisy/inconsistent
B. Clean data only
C. Hardware
D. Software install
Correct Answer: A

Q24. Data construction phase includes?
A. ETL + load + test
B. Requirement only
C. Design only
D. Admin only
Correct Answer: A

Q25. Metadata in warehouse is?
A. Data about data
B. User data
C. Fact data
D. Backup data
Correct Answer: A

Q26. Operational data store (ODS) is?
A. Current integrated for ops
B. Historical only
C. Archive only
D. External only
Correct Answer: A

Q27. Data mart is?
A. Departmental subset
B. Entire enterprise only
C. Source system
D. Staging only
Correct Answer: A

Q28. Dependent mart is fed from?
A. Warehouse
B. Source directly
C. Printer
D. User
Correct Answer: A

Q29. Independent mart is fed from?
A. Source directly
B. Warehouse only
C. OLAP
D. Browser
Correct Answer: A

Q30. Warehouse administration includes?
A. Security/backup/tuning
B. Coding only
C. Design only
D. Purchase only
Correct Answer: A

Q31. Roll-up operation?
A. Aggregate to higher level
B. Drill to detail
C. Slice only
D. Delete
Correct Answer: A

Q32. Drill-down operation?
A. Detail from aggregate
B. Aggregate only
C. Filter only
D. Delete
Correct Answer: A

Q33. Slice operation?
A. One dimension selection
B. All dims
C. No filter
D. Aggregation only
Correct Answer: A

Q34. Dice operation?
A. Multi-dim subcube
B. Single value
C. Delete cube
D. Create fact
Correct Answer: A

Q35. Pivot/rotate is?
A. Reorient cube view
B. Delete cube
C. Load data
D. Clean data
Correct Answer: A

Q36. MOLAP stores?
A. Multidimensional cubes
B. Relational only
C. Files only
D. No storage
Correct Answer: A

Q37. ROLAP stores?
A. Relational tables
B. Cubes only
C. XML only
D. Flat files
Correct Answer: A

Q38. HOLAP is?
A. Hybrid MOLAP+ROLAP
B. History only
C. High OLAP printer
D. Home OLAP
Correct Answer: A

Q39. Data cube lattice includes?
A. All cuboids/group-bys
B. Single table
C. No aggregation
D. Source only
Correct Answer: A

Q40. Iceberg cube stores only?
A. Cells meeting threshold
B. All cells
C. No cells
D. Dims only
Correct Answer: A

Q41. Warehouse design: top-down by?
A. Inmon
B. Kimball
C. Codd
D. Gray
Correct Answer: A

Q42. Bottom-up marts-first by?
A. Kimball
B. Inmon
C. Turing
D. Shannon
Correct Answer: A

Q43. Granularity means?
A. Level of detail
B. Data size in GB
C. User count
D. Table count
Correct Answer: A

Q44. Partitioning in warehouse helps?
A. Performance/manageability
B. Slow queries
C. More storage only
D. No use
Correct Answer: A

Q45. Indexing in warehouse e.g.?
A. Bitmap/join index
B. No index
C. Primary only
D. Sequential only
Correct Answer: A

Q46. Bitmap index best for?
A. Low-cardinality cols
B. High-cardinality
C. Text blobs
D. Images
Correct Answer: A

Q47. Materialized view stores?
A. Precomputed aggregates
B. Query text only
C. Source only
D. Metadata only
Correct Answer: A

Q48. View maintenance is?
A. Keep aggregates consistent
B. Delete views
C. Create users
D. Backup only
Correct Answer: A

Q49. Data warehouse analysis task?
A. OLAP/reporting/mining
B. Data entry
C. Transaction update
D. Deletion
Correct Answer: A

Q50. Backup/recovery in admin ensures?
A. Availability
B. Deletion
C. Slowness
D. Redundancy removal
Correct Answer: A

Q51. Data mining is?
A. Knowledge discovery from data
B. Digging coal
C. Data entry
D. Data deletion
Correct Answer: A

Q52. KDD steps order?
A. Selection/preprocess/transform/mine/evaluate
B. Mine first only
C. Evaluate first
D. No steps
Correct Answer: A

Q53. Data mining models include predictive/descriptive. Predictive is?
A. Classification/regression
B. Clustering only
C. Summarization only
D. Association only
Correct Answer: A

Q54. Descriptive models include?
A. Clustering/association
B. Classification only
C. Regression only
D. Prediction only
Correct Answer: A

Q55. Classification predicts?
A. Categorical label
B. Continuous value
C. Clusters
D. Sequences
Correct Answer: A

Q56. Regression predicts?
A. Numeric continuous
B. Class label
C. Cluster ID
D. Rule only
Correct Answer: A

Q57. Clustering is?
A. Unsupervised grouping
B. Supervised labeling
C. Regression
D. Classification
Correct Answer: A

Q58. Summarization gives?
A. Compact description
B. Full detail
C. Raw data
D. No output
Correct Answer: A

Q59. Dependency modeling finds?
A. Relationships/causality
B. No relation
C. Single attribute
D. Random data
Correct Answer: A

Q60. Link analysis finds?
A. Associations/links
B. No links
C. Single row
D. Sorting only
Correct Answer: A

Q61. Sequence analysis finds?
A. Ordered patterns over time
B. Unordered only
C. Static only
D. No order
Correct Answer: A

Q62. Association rule X=>Y support is?
A. P(X union Y)
B. P(Y|X) only
C. Count X only
D. Lift only
Correct Answer: A

Q63. Confidence of X=>Y is?
A. P(Y|X)
B. P(X)
C. P(Y)
D. Lift+support
Correct Answer: A

Q64. Lift >1 means?
A. Positive correlation
B. Negative
C. Independent
D. No rule
Correct Answer: A

Q65. Apriori principle?
A. Subset of frequent is frequent
B. Superset always frequent
C. No pruning
D. Random search
Correct Answer: A

Q66. Apriori join+prune uses?
A. L(k-1) to make Ck
B. Full scan always
C. No candidates
D. Decision tree
Correct Answer: A

Q67. Frequent itemset needs min?
A. Support threshold
B. Confidence only
C. Lift only
D. No threshold
Correct Answer: A

Q68. Strong rule needs min support + min?
A. Confidence
B. Lift only
C. Leverage only
D. Chi-square only
Correct Answer: A

Q69. FP-Growth avoids?
A. Candidate generation
B. Tree building
C. Scanning
D. Mining
Correct Answer: A

Q70. Decision tree internal node is?
A. Attribute test
B. Class label
C. Root only
D. Leaf only
Correct Answer: A

Q71. Decision tree leaf is?
A. Class label
B. Test
C. Split
D. Branch
Correct Answer: A

Q72. ID3 uses which measure?
A. Information gain
B. Gini only
C. Distance
D. Lift
Correct Answer: A

Q73. Entropy of pure set?
A. 0
B. 1
C. Max
D. Infinite
Correct Answer: A

Q74. Information gain is?
A. Entropy(parent)-weighted child
B. Child-parent
C. Gini+gain
D. Support
Correct Answer: A

Q75. Gini index used in?
A. CART
B. Apriori
C. K-means
D. PageRank
Correct Answer: A

Q76. Overfitting in trees handled by?
A. Pruning
B. Growing more
C. No validation
D. More depth always
Correct Answer: A

Q77. Prepruning stops?
A. Early by threshold
B. After full
C. Never
D. At leaves only
Correct Answer: A

Q78. Postpruning?
A. Grow full then trim
B. Stop early
C. No tree
D. Random cut
Correct Answer: A

Q79. Naive Bayes assumes?
A. Conditional independence
B. Dependence always
C. No probability
D. No prior
Correct Answer: A

Q80. Bayes theorem P(H|X)=?
A. P(X|H)P(H)/P(X)
B. P(X)/P(H)
C. P(H)+P(X)
D. P(H)-P(X)
Correct Answer: A

Q81. k-NN is?
A. Lazy instance-based
B. Eager tree
C. Rule-based
D. Neural only
Correct Answer: A

Q82. k-means is for?
A. Clustering
B. Classification
C. Regression
D. Association
Correct Answer: A

Q83. k-means steps?
A. Init assign update repeat
B. Sort only
C. Prune only
D. Split only
Correct Answer: A

Q84. k-means distance commonly?
A. Euclidean
B. Support
C. Confidence
D. Entropy
Correct Answer: A

Q85. k-means drawback?
A. Sensitive to k/init/outliers
B. No drawback
C. Supervised
D. Handles categorical well
Correct Answer: A

Q86. k-medoids uses?
A. Actual medoid object
B. Mean always
C. No center
D. Mode only
Correct Answer: A

Q87. PAM stands for?
A. Partitioning Around Medoids
B. Pattern Mining
C. Principal Mining
D. Probability Model
Correct Answer: A

Q88. Hierarchical clustering types?
A. Agglomerative/divisive
B. Flat only
C. Density only
D. Grid only
Correct Answer: A

Q89. AGNES is?
A. Agglomerative
B. Divisive
C. Density
D. Grid
Correct Answer: A

Q90. DIANA is?
A. Divisive
B. Agglomerative
C. Partitioning
D. Model-based
Correct Answer: A

Q91. Dendrogram shows?
A. Merge/split hierarchy
B. Decision boundary
C. ROC
D. Lift chart
Correct Answer: A

Q92. DBSCAN groups by?
A. Density
B. k centers
C. Hierarchy
D. Grid only
Correct Answer: A

Q93. DBSCAN core point needs minPts within?
A. Eps
B. k
C. Support
D. Confidence
Correct Answer: A

Q94. Outlier in DBSCAN is?
A. Noise point
B. Core always
C. Border always
D. Cluster center
Correct Answer: A

Q95. Regression linear model y=?
A. a+bx
B. a/b
C. Cluster
D. Rule
Correct Answer: A

Q96. Least squares minimizes?
A. Sum squared errors
B. Support
C. Entropy
D. Gain
Correct Answer: A

Q97. Multiple regression has?
A. Multiple predictors
B. One predictor
C. No predictor
D. Class label
Correct Answer: A

Q98. Logistic regression predicts?
A. Probability/class
B. Continuous only
C. Clusters
D. Rules
Correct Answer: A

Q99. Neural network learning via?
A. Backpropagation
B. Apriori
C. K-means
D. Pruning
Correct Answer: A

Q100. SVM finds?
A. Max-margin hyperplane
B. Decision tree
C. Clusters
D. Rules
Correct Answer: A

Q101. Mining scientific data challenge?
A. High-dim/noisy/experiments
B. Simple transactions only
C. No noise
D. Small data
Correct Answer: A

Q102. Mining business data uses?
A. RFM/churn/basket
B. DNA only
C. Spectra only
D. Images only
Correct Answer: A

Q103. Market basket data is?
A. Transactional items
B. Time series only
C. Spatial only
D. Text only
Correct Answer: A

Q104. Churn prediction is?
A. Classification
B. Clustering only
C. Association only
D. Sorting
Correct Answer: A

Q105. Credit scoring is?
A. Classification/risk
B. Clustering only
C. Summarization
D. Sequencing
Correct Answer: A

Q106. Fraud detection uses?
A. Outlier/anomaly
B. Sorting only
C. Reporting only
D. OLTP only
Correct Answer: A

Q107. Web mining types?
A. Content/structure/usage
B. Only content
C. Only hardware
D. Only cables
Correct Answer: A

Q108. Text mining steps?
A. Tokenize/stem/mine
B. Mine without clean
C. Hardware setup
D. No preprocessing
Correct Answer: A

Q109. TF-IDF measures?
A. Term importance
B. Support
C. Confidence
D. Distance
Correct Answer: A

Q110. Sequential pattern e.g.?
A. Buys A then B
B. Buys A and B unordered
C. Cluster
D. Regression
Correct Answer: A

Q111. GSP algorithm mines?
A. Sequential patterns
B. Decision trees
C. Clusters
D. Outliers
Correct Answer: A

Q112. Time-series mining finds?
A. Trends/seasonality
B. Static rules
C. No time
D. Spatial only
Correct Answer: A

Q113. Spatial mining considers?
A. Location/adjacency
B. Time only
C. No space
D. Transactions only
Correct Answer: A

Q114. Multimedia mining mines?
A. Image/audio/video
B. Numbers only
C. Text only
D. Transactions only
Correct Answer: A

Q115. Feature selection helps by?
A. Reduce dims/overfit
B. Increase dims
C. Add noise
D. Remove labels
Correct Answer: A

Q116. Data discretization converts?
A. Continuous to categorical
B. Categorical to continuous
C. Text to image
D. Numbers to noise
Correct Answer: A

Q117. Normalization range 0-1 is?
A. Min-max
B. Z-score
C. Decimal
D. No norm
Correct Answer: A

Q118. Z-score uses?
A. Mean/stddev
B. Min/max
C. Median only
D. Mode
Correct Answer: A

Q119. Missing values handled by?
A. Ignore/fill/mean
B. Delete DB
C. Stop mining
D. Ignore mining
Correct Answer: A

Q120. Noisy data smoothed by?
A. Binning/regression
B. No smoothing
C. Deletion only
D. Encryption
Correct Answer: A

Q121. Binning methods?
A. Equal-width/equal-freq
B. Random only
C. No bins
D. Single bin
Correct Answer: A

Q122. Correlation analysis detects?
A. Redundant attributes
B. Useful always keep all
C. No relation
D. Outliers only
Correct Answer: A

Q123. Chi-square for?
A. Categorical correlation
B. Numeric regression
C. Clustering
D. Classification label
Correct Answer: A

Q124. Evaluation: accuracy is?
A. Correct/total
B. TP/FP
C. FP only
D. TN only
Correct Answer: A

Q125. Precision is?
A. TP/(TP+FP)
B. TN/total
C. TP/FN
D. Accuracy
Correct Answer: A

Q126. Recall is?
A. TP/(TP+FN)
B. TP/(TP+FP)
C. TN/FP
D. Accuracy
Correct Answer: A

Q127. F1 is?
A. Harmonic mean P/R
B. Mean accuracy
C. Sum P+R
D. Max P,R
Correct Answer: A

Q128. Confusion matrix shows?
A. Actual vs predicted
B. Support only
C. Distance
D. Lift
Correct Answer: A

Q129. Cross-validation is for?
A. Reliable estimate
B. Faster training
C. More overfit
D. Less data use
Correct Answer: A

Q130. Holdout method splits?
A. Train/test
B. Train only
C. Test only
D. No split
Correct Answer: A

Q131. ROC plots?
A. TPR vs FPR
B. Precision vs support
C. Recall vs accuracy
D. Lift vs time
Correct Answer: A

Q132. AUC higher means?
A. Better classifier
B. Worse
C. Random
D. No model
Correct Answer: A

Q133. Underfitting means?
A. Too simple/high bias
B. Too complex
C. Perfect fit
D. No bias
Correct Answer: A

Q134. Overfitting means?
A. Too complex/high variance
B. Too simple
C. Perfect generalize
D. No variance
Correct Answer: A

Q135. Ensemble combines?
A. Multiple models
B. Single model
C. No models
D. Single tree only
Correct Answer: A

Q136. Bagging e.g.?
A. Random Forest
B. Single tree
C. K-means
D. Apriori
Correct Answer: A

Q137. Boosting e.g.?
A. AdaBoost
B. K-means
C. Apriori
D. DBSCAN
Correct Answer: A

Q138. Random Forest uses?
A. Bagged trees+random features
B. Single tree
C. Rules only
D. Linear only
Correct Answer: A

Q139. Warehouse vs database: warehouse is?
A. Read-only analytical
B. Update-heavy
C. Real-time writes
D. Volatile
Correct Answer: A

Q140. Nonvolatile means?
A. Stable no updates
B. Frequent updates
C. Deleted often
D. Temporary
Correct Answer: A

Q141. Time-variant means?
A. Historical time-stamped
B. Current only
C. No time
D. Real-time only
Correct Answer: A

Q142. Integrated means?
A. Unified schemas/formats
B. Separate formats
C. Isolated
D. Redundant conflicts kept
Correct Answer: A

Q143. Subject-oriented means?
A. Around themes (sales/customer)
B. Around apps
C. Around hardware
D. Around users login
Correct Answer: A

Q144. ETL tool example?
A. Informatica
B. MS Word
C. Photoshop
D. Browser
Correct Answer: A

Q145. OLAP tool example?
A. Cognos/MicroStrategy
B. Notepad
C. Paint
D. Compiler
Correct Answer: A

Q146. Data cube operation slice+dice helps?
A. Business analysis
B. Data entry
C. Transaction
D. Backup
Correct Answer: A

Q147. Dashboard shows?
A. KPIs/visuals
B. Raw logs
C. Code
D. Hardware
Correct Answer: A

Q148. Reports in warehouse are?
A. Predefined/ad-hoc
B. No reports
C. Code listings
D. Logs only
Correct Answer: A

Q149. Security in warehouse via?
A. Roles/access control
B. Open access
C. No passwords
D. Shared login
Correct Answer: A

Q150. Scalability needed due to?
A. Volume growth
B. Small data
C. Fixed size
D. No growth
Correct Answer: A

Q151. Apriori example: milk=>bread s=30% c=60% means?
A. 30% transactions both, 60% milk buyers buy bread
B. 60% all buy
C. 30% bread only
D. No meaning
Correct Answer: A

Q152. Closed frequent itemset?
A. No superset same support
B. All subsets
C. Max length only
D. Empty set
Correct Answer: A

Q153. Max frequent itemset?
A. No superset frequent
B. All frequent
C. Closed only
D. Single item
Correct Answer: A

Q154. Rule pruning by?
A. Min confidence/lift
B. Max support only
C. No pruning
D. Random delete
Correct Answer: A

Q155. Decision tree split for continuous?
A. Threshold/binary split
B. No split
C. Categorical only
D. Random
Correct Answer: A

Q156. C4.5 uses?
A. Gain ratio
B. Gini only
C. Distance
D. Support
Correct Answer: A

Q157. CART produces?
A. Binary trees
B. N-ary always
C. No tree
D. Forest only
Correct Answer: A

Q158. Tree induction complexity due to?
A. Attribute selection/partition
B. No computation
C. Sorting only
D. Printing
Correct Answer: A

Q159. Rule extraction from tree by?
A. Root-to-leaf paths
B. Leaf only
C. Random
D. Prune only
Correct Answer: A

Q160. k-means k chosen by?
A. Elbow/domain
B. Random fixed 1
C. Always 2
D. No choice
Correct Answer: A

Q161. Empty cluster in k-means handled by?
A. Reinit/split largest
B. Stop
C. Delete all
D. Ignore
Correct Answer: A

Q162. Categorical clustering uses?
A. K-modes
B. K-means Euclidean
C. Regression
D. SVM
Correct Answer: A

Q163. Outlier detection methods?
A. Statistical/distance/density
B. Sorting only
C. Reporting only
D. OLTP
Correct Answer: A

Q164. Isolation Forest isolates?
A. Anomalies
B. Normal only
C. Clusters
D. Rules
Correct Answer: A

Q165. Mining DNA/sequential bio uses?
A. Sequence alignment/patterns
B. Basket only
C. Sales only
D. No mining
Correct Answer: A

Q166. Scientific visualization helps?
A. Interpret patterns
B. Hide patterns
C. Store data
D. Delete noise
Correct Answer: A

Q167. Business KPI example?
A. Sales/profit/churn
B. Gene length
C. Spectra
D. Temperature only
Correct Answer: A

Q168. CRM mining uses?
A. Segmentation/cross-sell
B. Gene mining
C. Spectra
D. No CRM
Correct Answer: A

Q169. Segmentation uses?
A. Clustering
B. Classification only
C. Regression only
D. Sorting
Correct Answer: A

Q170. Target marketing uses?
A. Classification/profiles
B. Random mail
C. No data
D. Mass only
Correct Answer: A

Q171. Risk management uses?
A. Regression/scoring
B. Clustering only
C. No model
D. Reports only
Correct Answer: A

Q172. Demand forecasting uses?
A. Regression/time series
B. Association only
C. Clustering only
D. Sorting
Correct Answer: A

Q173. Inventory optimization uses?
A. Association/forecast
B. Classification only
C. No mining
D. Manual only
Correct Answer: A

Q174. Web usage mining uses?
A. Logs/clickstreams
B. Content only
C. Hardware
D. Cables
Correct Answer: A

Q175. PageRank mines?
A. Web structure
B. Content only
C. Usage only
D. Hardware
Correct Answer: A

Q176. Collaborative filtering for?
A. Recommendations
B. Clustering only
C. Sorting
D. Indexing
Correct Answer: A

Q177. Content-based filtering uses?
A. Item features
B. User ratings only
C. No features
D. Random
Correct Answer: A

Q178. Data quality issues?
A. Incomplete/noisy/inconsistent
B. Perfect data
C. No issues
D. Large data only
Correct Answer: A

Q179. Concept hierarchy enables?
A. Multi-level drill
B. Single level
C. No aggregation
D. Flat analysis
Correct Answer: A

Q180. Star-net query model is for?
A. Multidimensional queries
B. Transactions
C. Backups
D. ETL code
Correct Answer: A

Q181. Data warehouse bus architecture shares?
A. Conformed dims
B. Facts only
C. Staging only
D. Tools only
Correct Answer: A

Q182. Lifecycle: operations phase monitors?
A. Usage/performance
B. Requirements only
C. Design only
D. Build only
Correct Answer: A

Q183. Change management in warehouse handles?
A. Source/schema evolution
B. No changes
C. Hardware color
D. Staff only
Correct Answer: A

Q184. Growth management plans for?
A. Volume/users
B. Shrinkage
C. Deletion
D. Downtime
Correct Answer: A

Q185. Cost-benefit of warehouse measured by?
A. ROI/decision value
B. Lines of code
C. Tables count
D. Disk weight
Correct Answer: A

Q186. Big data vs warehouse: big data is?
A. Volume/velocity/variety
B. Small structured only
C. Relational only
D. Static only
Correct Answer: A

Q187. Hadoop complements warehouse by?
A. Unstructured processing
B. Replace all BI
C. No use
D. Storage only small
Correct Answer: A

Q188. Cloud warehouse e.g.?
A. Snowflake/BigQuery/Redshift
B. Notepad
C. Paint
D. DOS
Correct Answer: A

Q189. Real-time warehouse enables?
A. Near-real-time BI
B. Batch only
C. Annual reports
D. No BI
Correct Answer: A

Q190. Active warehouse supports?
A. Tactical decisions/automation
B. Archive only
C. Static reports
D. No decisions
Correct Answer: A

Q191. Data lake vs warehouse: lake stores?
A. Raw multi-format
B. Modeled only
C. Aggregates only
D. Reports only
Correct Answer: A

Q192. ETT vs ETL: ELT loads then?
A. Transforms in target
B. No transform
C. Transforms before
D. Deletes
Correct Answer: A

Q193. Data governance ensures?
A. Quality/compliance
B. No rules
C. Open chaos
D. Deletion
Correct Answer: A

Q194. Master data management provides?
A. Single truth for entities
B. Multiple truths
C. No entities
D. Transactions only
Correct Answer: A

Q195. Slow query in warehouse solved by?
A. Aggregates/index/partition
B. More transactions
C. Delete warehouse
D. Smaller RAM
Correct Answer: A

Q196. Concurrency in warehouse is?
A. Many readers/few writers
B. Many writers
C. No readers
D. Single user
Correct Answer: A

Q197. Data mining languages include?
A. DMQL extensions
B. Only SQL
C. Only Java
D. Only HTML
Correct Answer: A

Q198. Privacy-preserving mining uses?
A. Anonymization/perturbation
B. Open publish
C. No privacy
D. Delete mining
Correct Answer: A

Q199. K-anonymity ensures?
A. Indistinguishable k-records
B. Unique IDs
C. No anonymity
D. Full disclosure
Correct Answer: A

Q200. Future trend in mining?
A. Stream/big data/AI integration
B. Manual ledgers
C. No automation
D. Paper reports
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
181-A 182-A 183-A 184-A 185-A 186-A 187-A 188-A 189-A 190-A
191-A 192-A 193-A 194-A 195-A 196-A 197-A 198-A 199-A 200-A
