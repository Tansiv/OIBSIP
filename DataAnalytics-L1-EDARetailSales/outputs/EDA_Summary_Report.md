# Retail Sales EDA — Summary Report

**Generated from:** `customer_shopping_data.csv`

**Rows analyzed:** 99,457 | **Columns:** 17

---

## Key Metrics

- **Total Transactions:** 99,457
- **Total Revenue:** 251,505,794.25
- **Average Transaction Value:** 2528.79
- **Date Range:** 2021-01-01 to 2023-03-08
- **Top Revenue Category:** Clothing
- **Highest Volume Category:** Clothing
- **Top Revenue Mall:** Mall of Istanbul
- **Leading Age Group by Revenue:** 35-44
- **Strongest Quarter:** 2022-Q3
- **Strongest Correlation Pair:** price vs total_amount (r=0.962)

---

## Phase-by-Phase Log

```

============================================================
PHASE 1 — DATA LOADING & INITIAL INSPECTION
============================================================
Rows loaded: 99,457 | Columns: 10
Missing values found: 0
Duplicate rows found: 0

============================================================
PHASE 2 — DATA CLEANING & FEATURE ENGINEERING
============================================================
Date range: 2021-01-01 to 2023-03-08
Total revenue represented: 251,505,794.25
Derived columns added: year, month, month_name, quarter, weekday, total_amount, age_group

============================================================
PHASE 3 — DESCRIPTIVE STATISTICS
============================================================
age: mean=43.43, median=43.00, mode=37.00, std=14.99
quantity: mean=3.00, median=3.00, mode=3.00, std=1.41
price: mean=689.26, median=203.30, mode=600.16, std=941.18
total_amount: mean=2528.79, median=600.17, mode=1200.32, std=4222.48
Saved figure: phase3_boxplots.png

============================================================
PHASE 4 — TIME SERIES ANALYSIS
============================================================
Saved figure: phase4_monthly_trend.png
Highest revenue month: Jul 2021 (10,311,119.68)
Lowest revenue month: Mar 2023 (2,514,146.79)
Saved figure: phase4_quarterly_trend.png
Strongest quarter: 2022-Q3 (29,326,937.83)

============================================================
PHASE 5 — CUSTOMER DEMOGRAPHICS ANALYSIS
============================================================
Saved figure: phase5_age_distribution.png
Saved figure: phase5_gender_split.png
Gender distribution: {'Female': 59482, 'Male': 39975}
Average spend by gender: {'Female': 2525.25, 'Male': 2534.05}
Leading age group by total revenue: 35-44

============================================================
PHASE 6 — PRODUCT / CATEGORY ANALYSIS
============================================================
Saved figure: phase6_category_revenue.png
Top revenue category: Clothing (113,996,791.04)
Highest transaction volume category: Clothing (34487 transactions)

============================================================
PHASE 7 — CORRELATION ANALYSIS
============================================================
Saved figure: phase7_correlation_heatmap.png
Strongest correlation pair: price vs total_amount (r = 0.962)

============================================================
PHASE 8 — NON-OBVIOUS INSIGHT
============================================================
Saved figure: phase8_mall_revenue.png
Saved figure: phase8_mall_category_heatmap.png
Top revenue mall: Mall of Istanbul (50,872,481.68)
Leading category per mall: {'Cevahir AVM': 'Clothing', 'Emaar Square Mall': 'Clothing', 'Forum Istanbul': 'Clothing', 'Istinye Park': 'Clothing', 'Kanyon': 'Clothing', 'Mall of Istanbul': 'Clothing', 'Metrocity': 'Clothing', 'Metropol AVM': 'Clothing', 'Viaport Outlet': 'Clothing', 'Zorlu Center': 'Clothing'}

============================================================
PHASE 9 — CONSOLIDATED KEY METRICS
============================================================
Total Transactions: 99,457
Total Revenue: 251,505,794.25
Average Transaction Value: 2528.79
Date Range: 2021-01-01 to 2023-03-08
Top Revenue Category: Clothing
Highest Volume Category: Clothing
Top Revenue Mall: Mall of Istanbul
Leading Age Group by Revenue: 35-44
Strongest Quarter: 2022-Q3
Strongest Correlation Pair: price vs total_amount (r=0.962)

Processed dataset saved to: H:\Data Analyst\OASIS INFOBYTE\OIBSIP\DataAnalytics-L1-EDARetailSales\data\processed\final_analyzed_dataset.csv
```

---

## Business Recommendations

1. Prioritize stock and shelf space for 'Clothing' at 'Mall of Istanbul', since this combination represents the single highest revenue concentration found in the data.

2. Build targeted campaigns around the 35-44 age segment, which generated the highest total revenue of any age bracket in this dataset.

3. Treat 'Clothing' as a high-frequency traffic driver even where it is not the top revenue earner, since its transaction count of 34,487 indicates strong recurring footfall that can be cross-sold into higher-margin categories.

4. Apply mall-specific category planning rather than a uniform chain-wide strategy, since the Phase 8 heatmap shows each mall location favors a different leading category.
