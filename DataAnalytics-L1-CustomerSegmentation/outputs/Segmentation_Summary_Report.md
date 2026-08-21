# Customer Segmentation — Full Analysis Summary Report

**Generated from:** `online_retail_II.csv`

**Customers analyzed:** 5,878 | **Segments found:** 2

---

## Key Metrics

- **Total valid transactions:** 779,425
- **Total revenue:** 17,374,804.25
- **Unique customers:** 5,878
- **Final K (clusters):** 2
- **Final silhouette score:** 0.4187
- **Strongest segment:** Higher-Value Customers

---

## Segment Profile Table

| Segment_Name           |   Recency_mean |   Frequency_mean |   Monetary_mean |   Customer_count |
|:-----------------------|---------------:|-----------------:|----------------:|-----------------:|
| Higher-Value Customers |          63.95 |            11.52 |         5822.97 |             2699 |
| Lower-Value Customers  |         317.97 |             1.85 |          521.74 |             3179 |

---

## Phase-by-Phase Findings

### Phase 1 — Data Acquisition & Inspection

Raw dataset contained 1,067,371 transactions. 22.8% lacked a CustomerID, 34,335 were exact duplicates, and 22,950 / 6,207 rows had invalid Quantity/Price values respectively — all addressed in Phase 2.

### Phase 2 — Data Cleaning

After removing cancellations, invalid values, duplicates, and rows without a CustomerID, 779,425 valid transactions remained across 5,878 unique customers, representing 17,374,804.25 in total attributable revenue.

### Phase 3 — Exploratory Data Analysis

Customer spend is right-skewed (mean 2955.90 vs. median 867.74), driven by a smaller group of high-value customers. 27.6% of customers have purchased only once, marking a likely distinct low-engagement segment. Transaction volume peaked in Nov 2011.

### Phase 4 — RFM Feature Engineering

RFM features were built for 5,878 customers using a snapshot date of 2011-12-10. Frequency and Monetary were right-skewed in raw form, so log-transformed versions were created specifically for clustering while original values were preserved for business-facing profiling.

### Phase 5 — Standardization

Recency, log-Frequency, and log-Monetary were standardized to mean 0 / std 1 using StandardScaler, ensuring no single feature dominates K-Means distance calculations due to differing original scales.

### Phase 6 — K-Means Clustering & Elbow Method

K was selected using both the elbow curve and silhouette score, with K=2 chosen as it produced the highest silhouette score (0.419) among all tested values from 2 to 10 clusters.

### Phase 7 — Cluster Visualization

Three scatter plot pairs plus a combined pairplot confirmed visible separation between clusters across Recency, Frequency, and Monetary dimensions.

### Phase 8 — Cluster Profiling

2 clusters were profiled and automatically ranked into named segments based on relative Recency, Frequency, and Monetary performance. The strongest segment is 'Higher-Value Customers' with an average monetary value of 5822.97.

### Phase 9 — Cluster Size Visualization

Segment sizes range from 3,179 customers (Lower-Value Customers) down to 2,699 customers (Higher-Value Customers), shown in cluster_sizes.png.

### Phase 10 — Insights & Marketing Recommendations

Each segment was paired with a recommended marketing action derived from its relative rank in Recency, Frequency, and Monetary — prioritizing retention for top segments and re-engagement for weaker ones.

### Phase 11 — Final Packaging & Export

All 12 expected figures and the final labeled RFM dataset were verified and saved to disk, completing the pipeline end to end.

---

## Full Execution Log

```

=================================================================
PHASE 1 — DATA ACQUISITION & STRUCTURAL INSPECTION
=================================================================
Raw rows loaded: 1,067,371 | Columns: 8
Missing CustomerID: 22.77% of rows
Duplicate rows: 34,335
Rows with Quantity <= 0: 22,950
Rows with UnitPrice <= 0: 6,207

=================================================================
PHASE 2 — DATA CLEANING & CONSISTENCY HANDLING
=================================================================
Rows after cleaning: 779,425 (retained 73.0% of raw rows)
Unique customers: 5,878
Unique invoices: 36,969
Total revenue represented: 17,374,804.25
Saved: H:\Data Analyst\OASIS INFOBYTE\OIBSIP\DataAnalytics-L1-CustomerSegmentation\data\processed\cleaned_transactions.csv

=================================================================
PHASE 3 — EXPLORATORY DATA ANALYSIS & DESCRIPTIVE STATISTICS
=================================================================
Average total spend per customer: 2955.90
Median total spend per customer: 867.74
One-time buyers: 1,623 (27.6% of customer base)
Saved figure: spend_distribution.png
Saved figure: frequency_distribution.png
Saved figure: monthly_transaction_volume.png
Peak transaction month: Nov 2011 (63,168 transactions)

=================================================================
PHASE 4 — FEATURE ENGINEERING: RFM CONSTRUCTION
=================================================================
RFM table built for 5,878 unique customers
Snapshot date used: 2011-12-10
Recency range: 1 to 739 days
Frequency range: 1 to 398 orders
Monetary range: 2.95 to 580987.04
Saved figure: rfm_raw_distributions.png
Saved figure: rfm_log_distributions.png
Saved: H:\Data Analyst\OASIS INFOBYTE\OIBSIP\DataAnalytics-L1-CustomerSegmentation\data\processed\rfm_table.csv

=================================================================
PHASE 5 — STANDARDIZATION
=================================================================
Features scaled: ['Recency', 'Frequency_log', 'Monetary_log']
Post-scaling mean (expected ~0): {'Recency': -0.0, 'Frequency_log': 0.0, 'Monetary_log': -0.0}
Post-scaling std (expected ~1): {'Recency': 1.0, 'Frequency_log': 1.0, 'Monetary_log': 1.0}

=================================================================
PHASE 6 — K-MEANS CLUSTERING & ELBOW METHOD
=================================================================
Saved figure: elbow_curve.png
Saved figure: silhouette_scores.png
K selected by highest silhouette score: K=2
Final model fitted with K=2
Final silhouette score: 0.4187
Customers per cluster: {0: 3179, 1: 2699}

=================================================================
PHASE 7 — CLUSTER VISUALIZATION
=================================================================
Saved figure: scatter_recency_monetary.png
Saved figure: scatter_frequency_monetary.png
Saved figure: scatter_recency_frequency.png
Saved figure: rfm_pairplot.png

=================================================================
PHASE 8 — CLUSTER PROFILING
=================================================================
Cluster ranking (best to weakest behavioural profile): [1, 0]
Auto-assigned segment names: {1: 'Higher-Value Customers', 0: 'Lower-Value Customers'}

Note: These names are assigned programmatically based on relative rank across Recency/Frequency/Monetary. Review the numeric profile below and rename manually in your notebook if a more precise label fits your actual data better.

Segment profile summary:
                        Recency_mean  Frequency_mean  Monetary_mean  Customer_count
Segment_Name                                                                       
Higher-Value Customers         63.95           11.52        5822.97            2699
Lower-Value Customers         317.97            1.85         521.74            3179

=================================================================
PHASE 9 — CLUSTER SIZE VISUALIZATION
=================================================================
Saved figure: cluster_sizes.png
Segment size breakdown:
 - Lower-Value Customers: 3,179 customers (54.1%)
 - Higher-Value Customers: 2,699 customers (45.9%)

=================================================================
PHASE 10 — INSIGHTS & MARKETING RECOMMENDATIONS
=================================================================

Segment: Higher-Value Customers
  Size: 2,699 customers (45.9% of base)
  Recency=64.0d | Frequency=11.5 | Monetary=5822.97
  Recommended action: Prioritize retention offers and personalized outreach given their above-average spend and engagement.

Segment: Lower-Value Customers
  Size: 3,179 customers (54.1% of base)
  Recency=318.0d | Frequency=1.9 | Monetary=521.74
  Recommended action: Focus on low-cost, automated re-engagement emails rather than high-touch campaigns given lower spend levels.

=================================================================
PHASE 11 — FINAL PACKAGING & EXPORT
=================================================================
Final labeled RFM table saved to: H:\Data Analyst\OASIS INFOBYTE\OIBSIP\DataAnalytics-L1-CustomerSegmentation\data\processed\rfm_clustered.csv
Figures expected: 12 | Found: 13
All expected figures confirmed saved.
```
